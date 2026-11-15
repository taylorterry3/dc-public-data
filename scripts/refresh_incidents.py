"""Download, validate and stage annual MPD incidents. No Git or publishing side effects."""

import argparse
import hashlib
import json
import os
import re
import shutil
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen
from zoneinfo import ZoneInfo

import pandas as pd

from scripts.etl.common import data_cleanup

SERVICE = "https://maps2.dcgis.dc.gov/dcgis/rest/services/FEEDS/MPD/FeatureServer"
DATES = ("REPORT_DAT", "START_DATE", "END_DATE")
COLUMNS = (
    "X,Y,CCN,REPORT_DAT,SHIFT,METHOD,OFFENSE,BLOCK,XBLOCK,YBLOCK,WARD,ANC,DISTRICT,PSA,"
    "NEIGHBORHOOD_CLUSTER,BLOCK_GROUP,CENSUS_TRACT,VOTING_PRECINCT,LATITUDE,LONGITUDE,"
    "BID,START_DATE,END_DATE,OBJECTID,OCTO_RECORD_ID"
).split(",")


def request_json(url, **params):
    """Bounded retries for public, read-only requests; ArcGIS errors are fatal."""
    target = url + "?" + urlencode({"f": "json", **params})
    for attempt in range(3):
        try:
            with urlopen(target, timeout=90) as response:
                result = json.load(response)
            break
        except (OSError, ValueError):
            if attempt == 2:
                raise
            time.sleep(2 ** attempt)
    if "error" in result:
        raise ValueError(f"ArcGIS error at {url}: {result['error']}")
    return result


def discover(fetch=request_json):
    layers = {}
    for layer in fetch(SERVICE).get("layers", []):
        match = re.fullmatch(r"Crime Incidents - (\d{4})", layer["name"], re.IGNORECASE)
        if match:
            year = int(match[1])
            if year in layers:
                raise ValueError(f"Ambiguous annual layers for {year}")
            layers[year] = layer["id"]
    if not layers:
        raise ValueError("No annual incident layers discovered")
    return layers


def download(year, layer, fetch=request_json):
    """Fetch an ID snapshot in bounded batches and reconcile it after downloading."""
    url = f"{SERVICE}/{layer}"
    metadata = fetch(url)
    fields = {f["name"]: f["type"] for f in metadata["fields"]}
    missing = set(COLUMNS) - {"X", "Y"} - fields.keys()
    if missing or metadata.get("objectIdField") != "OBJECTID":
        raise ValueError(f"{year}: incompatible schema or row identifier: {sorted(missing)}")
    query = url + "/query"

    def ids():
        values = fetch(query, where="1=1", returnIdsOnly="true").get("objectIds")
        if not values or len(values) != len(set(values)):
            raise ValueError(f"{year}: empty or duplicate source row IDs")
        return sorted(values)

    expected = ids()
    batch_size = min(int(metadata.get("maxRecordCount", 1000)), 500)
    if batch_size < 1:
        raise ValueError(f"{year}: invalid source record limit")
    rows = []
    for offset in range(0, len(expected), batch_size):
        batch = expected[offset:offset + batch_size]
        result = fetch(
            query, objectIds=",".join(map(str, batch)), outFields="*",
            returnGeometry="true", outSR="26985",
        )
        if result.get("exceededTransferLimit"):
            raise ValueError(f"{year}: truncated batch")
        features = result.get("features", [])
        received = [f["attributes"].get("OBJECTID") for f in features]
        if len(received) != len(batch) or set(received) != set(batch):
            raise ValueError(f"{year}: incomplete or duplicate batch")
        for feature in features:
            row = feature["attributes"].copy()
            geometry = feature.get("geometry") or {}
            row.update(X=geometry.get("x"), Y=geometry.get("y"))
            rows.append(row)
    if ids() != expected:
        raise ValueError(f"{year}: source changed during download; retry the run")
    df = pd.DataFrame(rows)
    for col in DATES:
        if fields[col] != "esriFieldTypeDate":
            raise ValueError(f"{year}: unexpected date type for {col}")
        parsed = pd.to_datetime(df[col], unit="ms", utc=True, errors="raise")
        df[col] = parsed.dt.strftime("%Y-%m-%dT%H:%M:%SZ").fillna("")
    return df[COLUMNS].sort_values("OBJECTID").reset_index(drop=True)


def validate(df, year, old=None):
    missing = set(COLUMNS) - set(df.columns)
    if missing or df.empty:
        raise ValueError(f"{year}: empty data or missing columns {sorted(missing)}")
    for col in ("OBJECTID", "CCN", "REPORT_DAT", "OFFENSE"):
        if df[col].isna().any() or df[col].astype(str).eq("").any():
            raise ValueError(f"{year}: null required value in {col}")
    if df.OBJECTID.astype(str).duplicated().any():
        raise ValueError(f"{year}: duplicate OBJECTID")
    report_dates = pd.to_datetime(df.REPORT_DAT, format="mixed", utc=True, errors="raise")
    if not report_dates.dt.tz_convert("America/New_York").dt.year.eq(year).all():
        raise ValueError(f"{year}: report dates outside the annual dataset")
    pd.to_datetime(df.START_DATE.replace("", None), format="mixed", utc=True, errors="raise")
    pd.to_datetime(df.END_DATE.replace("", None), format="mixed", utc=True, errors="raise")
    if old is not None and len(df) < len(old):
        raise ValueError(f"{year}: record count decreased ({len(old)} -> {len(df)})")


def read_csv(path):
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def refresh(
    root, *, full_history=False, marker=None, now=None, fetch=request_json, accepted_root=None,
):
    """Validate every attempted year before promoting any files into the checkout."""
    now = now or datetime.now(ZoneInfo("America/New_York"))
    month = now.strftime("%Y-%m")
    if marker is not None:
        full_history |= not marker.exists() or marker.read_text().strip() != month
    raw = root / "data/raw"
    baseline = (accepted_root or root) / "data/raw"
    existing = {
        int(p.stem.rsplit("_", 1)[1]): p
        for p in raw.glob("Crime_Incidents_in_*.csv")
    }
    if not existing:
        raise ValueError("No accepted annual files found; refusing an unbounded initial import")
    layers = discover(fetch)
    missing = set(existing) - layers.keys()
    if missing:
        raise ValueError(f"Accepted years absent from source inventory: {sorted(missing)}")
    candidates = {y for y in layers if min(existing) <= y <= now.year}
    years = sorted(
        candidates if full_history else
        {y for y in candidates if y >= now.year - 1 or y not in existing}
    )
    if not years:
        raise ValueError("No recent published years to refresh")
    warnings = []
    if now.year not in layers:
        warnings.append(f"Current year {now.year} has not been published by the source.")
    results = []
    changed = []
    with tempfile.TemporaryDirectory(prefix="incident-refresh-") as temp:
        staging = Path(temp)
        for year in years:
            df = download(year, layers[year], fetch)
            accepted_path = baseline / f"Crime_Incidents_in_{year}.csv"
            old = read_csv(accepted_path) if accepted_path.exists() else None
            validate(df, year, old)
            print(f"Validated {year}: {len(df):,} rows", flush=True)
            path = staging / f"Crime_Incidents_in_{year}.csv"
            df.to_csv(path, index=False, lineterminator="\n")
            # Compare the canonical export bytes. Subsequent identical exports are no-ops.
            is_changed = year not in existing or path.read_bytes() != existing[year].read_bytes()
            if is_changed:
                changed.append((path, raw / path.name))
            results.append({
                "year": year, "source": f"{SERVICE}/{layers[year]}",
                "rows": len(df), "previous_rows": len(old) if old is not None else None,
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                "maximum_report_date": df.REPORT_DAT.max(), "changed": is_changed,
            })
        if changed:
            replacements = {dest.name: source for source, dest in changed}
            files = {p.name: p for p in existing.values()}
            files.update(replacements)
            combined = pd.concat(
                [read_csv(files[name]) for name in sorted(files)], ignore_index=True,
            )
            cleaned = data_cleanup(combined, "START_DATE")
            clean_path = staging / "incident_data.csv.gz"
            cleaned.to_csv(
                clean_path, index=False, compression={"method": "gzip", "mtime": 0},
            )
            changed.append((clean_path, root / "data/clean/incident_data.csv.gz"))
            # All downloads, validation and ETL have succeeded. Publish only staged files.
            for source, dest in changed:
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source, dest)
    # Marker lives in the workflow cache, not accepted data or the PR.
    if marker is not None and full_history:
        marker.parent.mkdir(parents=True, exist_ok=True)
        marker.write_text(month)
    return {
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "historical_sweep": full_history, "warnings": warnings, "years": results,
        "changed_files": [str(dest.relative_to(root)) for _, dest in changed],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--full-history", action="store_true")
    parser.add_argument("--accepted-root", type=Path, help="Accepted main snapshot for row counts")
    parser.add_argument("--history-marker", type=Path)
    parser.add_argument("--summary", type=Path, default=Path("/tmp/incident-refresh-summary.md"))
    args = parser.parse_args()
    try:
        result = refresh(
            args.root, full_history=args.full_history, marker=args.history_marker,
            accepted_root=args.accepted_root,
        )
        lines = ["## Annual incident refresh", "", f"Retrieved: {result['retrieved_at']}", ""]
        lines += result["warnings"]
        lines += ["", "| Year | Accepted rows | Downloaded rows | Changed |",
                  "| --- | --- | --- | --- |"]
        for item in result["years"]:
            lines.append(
                f"| {item['year']} | {item['previous_rows']} | {item['rows']} | "
                f"{item['changed']} |"
            )
        lines += ["", "Source URLs and export hashes:", "", "```json",
                  json.dumps(result, indent=2), "```", "", "Human review is required."]
        args.summary.write_text("\n".join(lines) + "\n")
        if output := os.environ.get("GITHUB_OUTPUT"):
            with open(output, "a") as stream:
                stream.write(f"changed={str(bool(result['changed_files'])).lower()}\n")
    except Exception as exc:
        args.summary.write_text(f"## Incident refresh failed\n\n{type(exc).__name__}: {exc}\n")
        raise


if __name__ == "__main__":
    main()

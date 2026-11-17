"""Download, validate and stage annual MPD incidents. No Git or publishing side effects."""

import argparse
import hashlib
import json
import logging
import os
import re
import shutil
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import urlopen
from zoneinfo import ZoneInfo

import pandas as pd

from scripts.etl.common import data_cleanup
from scripts.etl.incident_history import load_annual, normalize, reconcile

RETRYABLE_STATUS = {408, 429, 500, 502, 503, 504}
LOGGER = logging.getLogger(__name__)

SERVICE = "https://maps2.dcgis.dc.gov/dcgis/rest/services/FEEDS/MPD/FeatureServer"
DATES = ("REPORT_DAT", "START_DATE", "END_DATE")
COLUMNS = (
    "X,Y,CCN,REPORT_DAT,SHIFT,METHOD,OFFENSE,BLOCK,XBLOCK,YBLOCK,WARD,ANC,DISTRICT,PSA,"
    "NEIGHBORHOOD_CLUSTER,BLOCK_GROUP,CENSUS_TRACT,VOTING_PRECINCT,LATITUDE,LONGITUDE,"
    "BID,START_DATE,END_DATE,OBJECTID,OCTO_RECORD_ID"
).split(",")


def request_json(url, **params):
    """Retry transient public-source failures, including HTTP-200 ArcGIS errors."""
    target = url + "?" + urlencode({"f": "json", **params})
    for attempt in range(3):
        try:
            with urlopen(target, timeout=90) as response:
                result = json.load(response)
        except HTTPError as exc:
            if exc.code not in RETRYABLE_STATUS or attempt == 2:
                raise
        except (OSError, ValueError):
            if attempt == 2:
                raise
        else:
            if "error" not in result:
                return result
            error = result["error"]
            if error.get("code") not in RETRYABLE_STATUS or attempt == 2:
                raise ValueError(f"ArcGIS error at {url}: {error}")
        delay = 2 ** attempt
        LOGGER.warning("Transient source failure; retrying in %ss (attempt %s/3)",
                       delay, attempt + 1)
        time.sleep(delay)


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


def validate(df, year):
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
    history = root / "data/history/incidents"
    history_current = {
        int(p.parent.name): p for p in history.glob("*/current.csv.gz")
    }
    history_stats = {}
    with tempfile.TemporaryDirectory(prefix="incident-refresh-") as temp:
        staging = Path(temp)

        def stage_history(year, observed, old, observation_date):
            current_path = history / str(year) / "current.csv.gz"
            versions_path = history / str(year) / "versions.csv.gz"
            current = read_csv(current_path) if current_path.exists() else None
            versions = read_csv(versions_path) if versions_path.exists() else None
            # Import accepted data, not a potentially smaller pending raw snapshot.
            legacy = old if old is not None else observed.iloc[:0]
            current, versions, stats = reconcile(
                year, legacy, observed, current=current, versions=versions, on=observation_date,
            )
            history_stats[year] = stats
            for name, frame, dest in (
                ("current.csv.gz", current, current_path),
                ("versions.csv.gz", versions, versions_path),
            ):
                path = staging / "history" / str(year) / name
                path.parent.mkdir(parents=True, exist_ok=True)
                frame.to_csv(path, index=False, compression={"method": "gzip", "mtime": 0})
                if not dest.exists() or path.read_bytes() != dest.read_bytes():
                    changed.append((path, dest))
                if name == "current.csv.gz":
                    history_current[year] = path

        for year in years:
            df = download(year, layers[year], fetch)
            accepted_path = baseline / f"Crime_Incidents_in_{year}.csv"
            old = read_csv(accepted_path) if accepted_path.exists() else None
            validate(df, year)
            stage_history(year, df, old, now.strftime("%Y-%m-%d"))
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
                "maximum_report_date": df.REPORT_DAT.max(),
                "changed": not accepted_path.exists() or
                path.read_bytes() != accepted_path.read_bytes(),
                "updated_this_run": is_changed, "history": history_stats[year],
            })
        # A pre-history bot PR may contain historical raw changes with unknown
        # observation dates. Migrate them without inventing a fresh sighting.
        for year, path in existing.items():
            if year in years:
                continue
            accepted_path = baseline / path.name
            pending = read_csv(path)
            if year in history_current:
                current = read_csv(history_current[year])
                represented = current[current.present_in_latest_source == "true"][COLUMNS]
                differs = not normalize(pending).sort_values("OBJECTID").reset_index(
                    drop=True,
                ).equals(normalize(represented).sort_values("OBJECTID").reset_index(drop=True))
            else:
                differs = accepted_path.exists() and path.read_bytes() != accepted_path.read_bytes()
            if differs:
                old = read_csv(accepted_path) if accepted_path.exists() else None
                stage_history(year, pending, old, "")
        pending_raw = any(
            not (baseline / p.name).exists() or
            p.read_bytes() != (baseline / p.name).read_bytes()
            for p in existing.values()
        ) if accepted_root is not None else False
        clean_existing = root / "data/clean/incident_data.csv.gz"
        clean_baseline = (accepted_root or root) / "data/clean/incident_data.csv.gz"
        pending_clean = accepted_root is not None and clean_existing.exists() and (
            not clean_baseline.exists() or
            clean_existing.read_bytes() != clean_baseline.read_bytes()
        )
        if changed or pending_raw or pending_clean:
            replacements = {dest.name: source for source, dest in changed if dest.parent == raw}
            files = {p.name: p for p in existing.values()}
            files.update(replacements)
            combined = load_annual(
                {int(Path(name).stem.rsplit("_", 1)[1]): path for name, path in files.items()},
                history_current,
            )
            cleaned = data_cleanup(combined, "START_DATE")
            clean_path = staging / "incident_data.csv.gz"
            cleaned.to_csv(
                clean_path, index=False, compression={"method": "gzip", "mtime": 0},
            )
            clean_dest = root / "data/clean/incident_data.csv.gz"
            if not clean_dest.exists() or clean_path.read_bytes() != clean_dest.read_bytes():
                changed.append((clean_path, clean_dest))
        # Compare the complete candidate snapshot before replacing local baseline files.
        files = {p.name: p for p in existing.values()}
        files.update({dest.name: source for source, dest in changed if dest.parent == raw})
        pending_years = []
        pending_files = []
        for name, path in sorted(files.items()):
            accepted_path = baseline / name
            content = path.read_bytes()
            if accepted_path.exists() and content == accepted_path.read_bytes():
                continue
            year = int(path.stem.rsplit("_", 1)[1])
            df = read_csv(path)
            old = read_csv(accepted_path) if accepted_path.exists() else None
            validate(df, year)
            digest = hashlib.sha256(content).hexdigest()
            pending_years.append({
                "year": year, "source": f"{SERVICE}/{layers[year]}", "rows": len(df),
                "previous_rows": len(old) if old is not None else None,
                "sha256": digest, "maximum_report_date": df.REPORT_DAT.max(), "changed": True,
            })
            pending_files.append({"path": f"data/raw/{name}", "sha256": digest})
        clean_relative = Path("data/clean/incident_data.csv.gz")
        clean_candidate = next(
            (src for src, dest in changed if dest == root / clean_relative),
            root / clean_relative,
        )
        clean_accepted = (accepted_root or root) / clean_relative
        if clean_candidate.exists() and (
            not clean_accepted.exists() or
            clean_candidate.read_bytes() != clean_accepted.read_bytes()
        ):
            pending_files.append({
                "path": str(clean_relative),
                "sha256": hashlib.sha256(clean_candidate.read_bytes()).hexdigest(),
            })
        # History files are reviewable even on days with no raw source changes.
        history_candidates = {p.relative_to(root): p for p in history.glob("*/*.csv.gz")}
        history_candidates.update({
            dest.relative_to(root): src for src, dest in changed if history in dest.parents
        })
        pending_history = []
        for relative, path in sorted(history_candidates.items()):
            accepted_path = (accepted_root or root) / relative
            if not accepted_path.exists() or path.read_bytes() != accepted_path.read_bytes():
                pending_files.append({
                    "path": str(relative), "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                })
                if path.name == "current.csv.gz":
                    year = int(relative.parent.name)
                    current = read_csv(path)
                    version_relative = relative.with_name("versions.csv.gz")
                    version_path = history_candidates.get(version_relative)
                    pending_history.append({
                        "year": year, "source": f"{SERVICE}/{layers[year]}",
                        "source_rows": len(read_csv(files[f"Crime_Incidents_in_{year}.csv"])),
                        "retained_rows": len(current),
                        "absent_rows": int(current.present_in_latest_source.eq("false").sum()),
                        "archived_versions": len(read_csv(version_path)) if version_path else 0,
                    })
        # All downloads, validation, ETL and reporting have succeeded.
        if changed:
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
        "pending_years": pending_years, "pending_files": pending_files,
        "history": history_stats, "pending_history": pending_history,
        "changed_files": [str(dest.relative_to(root)) for _, dest in changed],
    }


def render_report(result, *, pending=False):
    """Keep download-run observations separate from the entire review snapshot."""
    years = result["pending_years"] if pending else result["years"]
    title = "Pending annual incident changes against accepted main" if pending else "Incident run"
    lines = [f"## {title}", "", f"Report generated: {result['retrieved_at']}", ""]
    lines += result["warnings"]
    lines += ["", "| Year | Accepted rows | Candidate rows | Differs from accepted main |",
              "| --- | --- | --- | --- |"]
    for item in years:
        lines.append(
            f"| {item['year']} | {item['previous_rows']} | {item['rows']} | {item['changed']} |"
        )
    payload = {"years": years, "files": result["pending_files"],
               "pending_history": result["pending_history"]} if pending else result
    if pending:
        lines += ["", "### Retained history pending review", "",
                  "| Year | Source rows | Retained records | Absent | Archived versions |",
                  "| --- | --- | --- | --- | --- |"]
        for item in result["pending_history"]:
            lines.append(
                f"| {item['year']} | {item['source_rows']} | {item['retained_rows']} | "
                f"{item['absent_rows']} | {item['archived_versions']} |"
            )
        lines += ["", "Includes preserved historical changes not downloaded this run.",
                  "Hashes describe the pending files; report time is not their retrieval time."]
    lines += ["", "Source URLs and export hashes:", "", "```json",
              json.dumps(payload, indent=2), "```", "", "Human review is required."]
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--full-history", action="store_true")
    parser.add_argument("--accepted-root", type=Path, help="Accepted main snapshot for row counts")
    parser.add_argument("--history-marker", type=Path)
    parser.add_argument("--summary", type=Path, default=Path("/tmp/incident-refresh-summary.md"))
    parser.add_argument("--pr-body", type=Path, help="Complete pending diff against accepted data")
    args = parser.parse_args()
    try:
        result = refresh(
            args.root, full_history=args.full_history, marker=args.history_marker,
            accepted_root=args.accepted_root,
        )
        args.summary.write_text(render_report(result))
        if args.pr_body is not None:
            args.pr_body.write_text(render_report(result, pending=True))
        if output := os.environ.get("GITHUB_OUTPUT"):
            with open(output, "a") as stream:
                stream.write(f"changed={str(bool(result['changed_files'])).lower()}\n")
    except Exception as exc:
        args.summary.write_text(f"## Incident refresh failed\n\n{type(exc).__name__}: {exc}\n")
        raise


if __name__ == "__main__":
    main()

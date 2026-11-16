"""Cache annual source exports, audit every ambiguous group, and replay locally.

Examples (all generated data stays under --cache-dir):
    python -m scripts.audit_incidents --cache-dir /tmp/incident-audit --download
    python -m scripts.audit_incidents --cache-dir /tmp/incident-audit
    python -m scripts.audit_incidents --cache-dir /tmp/incident-audit --replay
"""

import argparse
import hashlib
import json
import shutil
from collections import Counter, deque
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch
from zoneinfo import ZoneInfo

from scripts import refresh_incidents as refresh
from scripts.etl.incident_history import VOLATILE, normalize, reconcile


def write_json(path, value):
    temporary = path.with_name(path.name + ".partial")
    temporary.write_text(json.dumps(value, indent=2) + "\n")
    temporary.replace(path)


def capture(cache):
    """Download all published layers once; resume using verified frozen files."""
    cache.mkdir(parents=True, exist_ok=True)
    path = cache / "manifest.json"
    live_layers = refresh.discover()
    if path.exists():
        manifest = json.loads(path.read_text())
        layers = {int(y): layer for y, layer in manifest["layers"].items()}
        if layers != live_layers:
            raise ValueError("Source layer inventory changed; use a fresh cache directory")
    else:
        layers = live_layers
        manifest = {"exports": {}, "layers": layers}
        write_json(path, manifest)
    errors = []

    def export(year, layer):
        target = cache / f"Crime_Incidents_in_{year}.csv"
        previous = manifest["exports"].get(str(year))
        source = f"{refresh.SERVICE}/{layer}"
        if previous:
            if not target.exists() or previous["source"] != source or (
                hashlib.sha256(target.read_bytes()).hexdigest() != previous["sha256"]
            ):
                raise ValueError(f"{year}: recorded frozen export changed; use a fresh cache")
            return year, previous, True
        df = refresh.download(year, layer)
        refresh.validate(df, year)
        temp = target.with_suffix(".partial")
        df.to_csv(temp, index=False)
        temp.replace(target)
        return year, {
            "source": source, "rows": len(df),
            "retrieved_at": datetime.now(timezone.utc).isoformat(),
            "sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
        }, False

    with ThreadPoolExecutor(max_workers=3) as pool:
        tasks = {pool.submit(export, year, layer): year for year, layer in layers.items()}
        for task in as_completed(tasks):
            year = tasks[task]
            try:
                year, details, cached = task.result()
                manifest["exports"][str(year)] = details
                write_json(path, manifest)
                print(f"{'Cached' if cached else 'Downloaded'} {year}: {details['rows']:,} rows",
                      flush=True)
            except Exception as exc:
                errors.append({"year": year, "error": str(exc)})
                print(f"FAILED {year}: {exc}", flush=True)
    write_json(cache / "download-errors.json", errors)
    return not errors


def frozen(cache):
    manifest = json.loads((cache / "manifest.json").read_text())
    layers = {int(y): layer for y, layer in manifest["layers"].items()}
    for year in layers:
        path = cache / f"Crime_Incidents_in_{year}.csv"
        details = manifest["exports"].get(str(year))
        if not details or details["source"] != f"{refresh.SERVICE}/{layers[year]}" or (
            not path.exists()
        ) or (
            hashlib.sha256(path.read_bytes()).hexdigest() != details["sha256"]
        ):
            raise ValueError(f"Missing or altered frozen export: {year}; resume --download")
    return manifest, layers


def audit(root, cache):
    """Collect every problematic duplicate-CCN group, not just the first failure."""
    manifest, layers = frozen(cache)
    earliest = min(int(p.stem.rsplit("_", 1)[1])
                   for p in (root / "data/raw").glob("Crime_Incidents_in_*.csv"))
    result = {"years": [], "issues": []}
    for year in sorted(y for y in layers if y >= earliest):
        path = root / f"data/raw/Crime_Incidents_in_{year}.csv"
        observed = refresh.read_csv(cache / path.name)
        old = refresh.read_csv(path) if path.exists() else observed.iloc[:0]
        try:
            refresh.validate(observed, year)
            folder = root / f"data/history/incidents/{year}"
            current_path, versions_path = folder / "current.csv.gz", folder / "versions.csv.gz"
            current = refresh.read_csv(current_path) if current_path.exists() else None
            versions = refresh.read_csv(versions_path) if versions_path.exists() else None
            candidates = current if current is not None else old
            old_counts, new_counts = candidates.CCN.value_counts(), observed.CCN.value_counts()
            shared = old_counts.index.intersection(new_counts.index)
            groups = sorted(ccn for ccn in shared
                            if old_counts[ccn] > 1 or new_counts[ccn] > 1)
            old_groups = dict(tuple(candidates[candidates.CCN.isin(groups)].groupby("CCN")))
            baseline_groups = dict(tuple(old[old.CCN.isin(groups)].groupby("CCN")))
            new_groups = dict(tuple(observed[observed.CCN.isin(groups)].groupby("CCN")))
            problems = 0
            for ccn in groups:
                try:
                    observed_on = datetime.fromisoformat(
                        manifest["exports"][str(year)]["retrieved_at"],
                    ).astimezone(ZoneInfo("America/New_York")).date().isoformat()
                    retained = old_groups[ccn] if current is not None else None
                    archived = versions[versions.record_id.isin(retained.record_id)] if (
                        versions is not None and retained is not None
                    ) else None
                    reconcile(
                        year, baseline_groups.get(ccn, old.iloc[:0]), new_groups[ccn],
                        current=retained, versions=archived, on=observed_on,
                    )
                except ValueError as exc:
                    problems += 1
                    result["issues"].append({
                        "year": year, "ccn": ccn, "error": str(exc),
                        "accepted": old_groups[ccn].to_dict("records"),
                        "observed": new_groups[ccn].to_dict("records"),
                    })
            result["years"].append({"year": year, "accepted_rows": len(old),
                                    "source_rows": len(observed),
                                    "duplicate_groups": len(groups), "issues": problems})
            print(f"Audit {year}: {len(groups)} duplicate groups, {problems} issues", flush=True)
        except Exception as exc:
            result["issues"].append({"year": year, "error": str(exc)})
            print(f"Audit {year} FAILED: {exc}", flush=True)
    write_json(cache / "audit.json", result)
    return not result["issues"]


def retention_expectation(root, year):
    """Freeze identity or occurrence evidence before replay can change its inputs."""
    path = root / f"data/history/incidents/{year}/current.csv.gz"
    if path.exists():
        return {"ids": set(refresh.read_csv(path).record_id)}
    path = root / f"data/raw/Crime_Incidents_in_{year}.csv"
    if not path.exists():
        return {"ids": set()}
    frame = refresh.read_csv(path)
    business = [c for c in frame.columns if c not in VOLATILE]
    counts = Counter(normalize(frame)[business].itertuples(index=False, name=None))
    return {"business": business, "columns": list(frame.columns), "occurrences": counts}


def verify_retention(year, current, versions, expected):
    """Counts cannot prove retention: check IDs or distinct occurrence witnesses."""
    if "ids" in expected:
        missing = expected["ids"] - set(current.record_id)
        if missing:
            raise ValueError(f"{year}: lost accepted retained record IDs ({len(missing)})")
        return
    wanted = expected["occurrences"]
    witnesses = {key: set() for key in wanted}
    for frame in (current, versions):
        canonical = normalize(frame[expected["columns"]])[expected["business"]]
        for key, record_id in zip(canonical.itertuples(index=False, name=None), frame.record_id):
            if key in witnesses:
                witnesses[key].add(record_id)
    # Assign a distinct retained ID to EVERY accepted occurrence globally.
    # One record with multiple old payload versions cannot witness two records.
    owners = {}
    for key, count in wanted.items():
        for _ in range(count):
            queue, seen, parents = deque([key]), {key}, {}
            assigned = False
            while queue and not assigned:
                candidate = queue.popleft()
                for record_id in witnesses[candidate]:
                    if record_id not in owners:
                        owners[record_id] = candidate
                        while candidate != key:
                            candidate, record_id = parents[candidate]
                            owners[record_id] = candidate
                        assigned = True
                        break
                    previous = owners[record_id]
                    if previous not in seen:
                        seen.add(previous)
                        parents[previous] = (candidate, record_id)
                        queue.append(previous)
    missing = sum(wanted.values()) - len(owners)
    if missing:
        raise ValueError(f"{year}: lost accepted raw occurrences ({missing})")


def replay(root, cache, name="replay", *, verify=False):
    """Run the production refresh with frozen downloads in a disposable data tree."""
    manifest, layers = frozen(cache)
    if Path(name).name != name or name in {".", ".."}:
        raise ValueError("Replay name must be a directory name")
    sandbox = cache / name
    if verify:
        if not sandbox.exists():
            raise ValueError("Run --replay before --verify-replay")
    else:
        if sandbox.exists():
            raise ValueError("Replay directory already exists; select a fresh --replay-name")
        (sandbox / "data/raw").mkdir(parents=True)
        for path in (root / "data/raw").glob("Crime_Incidents_in_*.csv"):
            shutil.copyfile(path, sandbox / "data/raw" / path.name)
        if (root / "data/history/incidents").exists():
            shutil.copytree(root / "data/history/incidents", sandbox / "data/history/incidents")

    def inventory(*args, **kwargs):
        return {"layers": [{"name": f"Crime Incidents - {y}", "id": layer}
                           for y, layer in layers.items()]}

    def cached_download(year, layer, fetch):
        return refresh.read_csv(cache / f"Crime_Incidents_in_{year}.csv")

    now = max(datetime.fromisoformat(item["retrieved_at"])
              for item in manifest["exports"].values()).astimezone(ZoneInfo("America/New_York"))
    earliest = min(int(p.stem.rsplit("_", 1)[1])
                   for p in (sandbox / "data/raw").glob("Crime_Incidents_in_*.csv"))
    expected = {year: retention_expectation(sandbox if verify else root, year)
                for year in layers if earliest <= year <= now.year}
    with patch.object(refresh, "download", cached_download):
        result = refresh.refresh(sandbox, accepted_root=root, full_history=True,
                                 now=now, fetch=inventory)
    if verify and result["changed_files"]:
        raise ValueError(f"Identical replay changed files: {result['changed_files']}")
    totals = {"source_rows": 0, "retained_rows": 0, "absent_rows": 0, "archived_versions": 0}
    for item in result["years"]:
        year = item["year"]
        source = sandbox / f"data/raw/Crime_Incidents_in_{year}.csv"
        if source.read_bytes() != (cache / source.name).read_bytes():
            raise ValueError(f"{year}: raw snapshot differs from frozen export")
        current = refresh.read_csv(sandbox / f"data/history/incidents/{year}/current.csv.gz")
        versions = refresh.read_csv(sandbox / f"data/history/incidents/{year}/versions.csv.gz")
        verify_retention(year, current, versions, expected[year])
        if current.present_in_latest_source.eq("true").sum() != item["rows"]:
            raise ValueError(f"{year}: published subset count mismatch")
        if len(versions) != (current.version.astype(int) - 1).sum():
            raise ValueError(f"{year}: archived version sequence/count mismatch")
        for field in totals:
            totals[field] += item["history"][field]
    cleaned = refresh.read_csv(sandbox / "data/clean/incident_data.csv.gz")
    if len(cleaned) != totals["retained_rows"] or cleaned.record_id.duplicated().any():
        raise ValueError("Cleaned output duplicated versions or lost retained records")
    result["verified_totals"] = totals
    suffix = "verification" if verify else "result"
    write_json(cache / f"{name}-{suffix}.json", result)
    (cache / f"{name}-summary.md").write_text(refresh.render_report(result))
    (cache / f"{name}-pr.md").write_text(refresh.render_report(result, pending=True))
    print(f"Full refresh passed: {len(result['years'])} years; output: {sandbox}", flush=True)
    print(f"Verified totals: {totals}", flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--cache-dir", type=Path, required=True)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--download", action="store_true")
    modes.add_argument("--replay", action="store_true")
    modes.add_argument("--verify-replay", action="store_true")
    parser.add_argument("--replay-name", default="replay")
    args = parser.parse_args()
    if args.download:
        ok = capture(args.cache_dir)
    elif args.replay or args.verify_replay:
        replay(args.root, args.cache_dir, args.replay_name, verify=args.verify_replay)
        ok = True
    else:
        ok = audit(args.root, args.cache_dir)
    raise SystemExit(0 if ok else 1)


if __name__ == "__main__":
    main()

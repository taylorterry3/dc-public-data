"""Reconcile complete annual observations without discarding missing records.

CCN scopes matching within a report year, but is not a unique row identifier.
Ambiguous revisions fail rather than guessing which occurrence changed.
"""

import hashlib
import json
from collections import defaultdict

import pandas as pd

META = [
    "record_id", "first_seen_on", "last_seen_on", "present_in_latest_source",
    "version", "version_first_seen_on", "version_last_seen_on", "baseline_imported_on",
]
VOLATILE = {"OBJECTID", "OCTO_RECORD_ID", "X", "Y"}
DATES = {"REPORT_DAT", "START_DATE", "END_DATE"}
NUMERIC = {"X", "Y", "XBLOCK", "YBLOCK", "LATITUDE", "LONGITUDE"}
ANCHOR = ("OFFENSE", "METHOD", "REPORT_DAT", "START_DATE", "BLOCK")
INTERVAL_ANCHOR = ("OFFENSE", "METHOD", "REPORT_DAT", "START_DATE", "END_DATE")


def normalize(frame):
    """Compare business values, not portal date/number formatting or reload IDs."""
    frame = frame.copy().fillna("").astype(str)
    for column in frame.columns:
        if column in DATES:
            parsed = pd.to_datetime(frame[column].replace("", None), format="mixed", utc=True)
            frame[column] = parsed.dt.strftime("%Y-%m-%dT%H:%M:%SZ").fillna("")
        elif column in NUMERIC:
            frame[column] = frame[column].map(lambda v: format(float(v), ".6f") if v else "")
        elif column == "BLOCK":
            frame[column] = frame[column].str.replace(r"\s+", " ", regex=True).str.strip()
        elif column == "CCN":
            numeric = frame[column].str.fullmatch(r"\d+")
            frame.loc[numeric, column] = frame.loc[numeric, column].str.zfill(8)
    return frame


def signature(row, columns):
    canonical = row.get("_normalized", row)
    return tuple(canonical[c] for c in columns)


def reconcile(year, baseline, observed, *, current=None, versions=None, on):
    """Return current records, superseded versions and counts; no file writes.

    Dates are local observation dates, not incident dates. Baseline imports have
    unknown first/last observation dates. A nonempty observation date requires
    a complete download; an empty date imports a legacy snapshot without
    asserting a fresh sighting. Publisher OIDs never establish continuity.
    """
    columns = list(observed.columns)
    business = [c for c in columns if c not in VOLATILE]

    def payloads(frame):
        values = frame[columns].fillna("").astype(str).to_dict("records")
        canonical = normalize(frame[columns]).to_dict("records")
        for value, comparable in zip(values, canonical):
            value["_normalized"] = comparable
        return values

    observations = payloads(observed)
    if current is not None and (
        current.record_id.isna().any() or current.record_id.eq("").any() or
        current.record_id.duplicated().any()
    ):
        raise ValueError(f"{year}: invalid retained record identifiers")
    if versions is not None and versions.duplicated(["record_id", "version"]).any():
        raise ValueError(f"{year}: duplicate archived versions")
    used = set() if current is None else set(current.record_id)

    def new_record(row, imported=False):
        seed = json.dumps([year, signature(row, business)], separators=(",", ":"))
        rank = 0
        while True:
            record_id = hashlib.sha256(f"{seed}:{rank}".encode()).hexdigest()
            if record_id not in used:
                break
            rank += 1
        used.add(record_id)
        return {**row, "record_id": record_id, "first_seen_on": "", "last_seen_on": "",
                "present_in_latest_source": "", "version": "1",
                "version_first_seen_on": "", "version_last_seen_on": "",
                "baseline_imported_on": on if imported else ""}

    if current is None:
        records = [new_record(row, imported=True)
                   for row in payloads(baseline)]
    else:
        records = payloads(current)
        for record, meta in zip(records, current[META].fillna("").astype(str).to_dict("records")):
            record.update(meta)
    archived = [] if versions is None else versions.fillna("").astype(str).to_dict("records")
    old_groups, new_groups = defaultdict(list), defaultdict(list)
    for index, row in enumerate(records):
        old_groups[row["CCN"]].append(index)
    for index, row in enumerate(observations):
        new_groups[row["CCN"]].append(index)
    pairs, additions = [], []
    for ccn, incoming in new_groups.items():
        old = sorted(old_groups[ccn], key=lambda i: (
            records[i]["present_in_latest_source"] != "true", records[i]["record_id"],
        ))
        remaining = list(incoming)

        def match_by(fields):
            old_matches, new_matches = defaultdict(list), defaultdict(list)
            for previous in old:
                old_matches[signature(records[previous], fields)].append(previous)
            for new in remaining:
                new_matches[signature(observations[new], fields)].append(new)
            for key, incoming_matches in new_matches.items():
                candidates = old_matches[key]
                if not candidates:
                    continue
                # Check the entire group on BOTH sides before consuming any
                # match. Only business-equivalent duplicates are interchangeable.
                if len({signature(records[i], business) for i in candidates}) > 1 or len({
                    signature(observations[i], business) for i in incoming_matches
                }) > 1:
                    continue
                for new in incoming_matches:
                    if not candidates:
                        break
                    # Publisher IDs only break ties between equivalent payloads.
                    previous = next((i for i in candidates if records[i]["OBJECTID"] ==
                                     observations[new]["OBJECTID"]), candidates[0])
                    pairs.append((previous, new))
                    candidates.remove(previous)
                    old.remove(previous)
                    remaining.remove(new)

        match_by(business)
        # Exact values reconnect missing/reappearing records before corrections.
        match_by(ANCHOR)
        # A publisher may correct a block range as well as its coordinates.
        # Keep the complete time interval and offense/method fixed, and retain
        # the same two-sided equivalence guard as every other matching pass.
        match_by(INTERVAL_ANCHOR)
        if old and remaining:
            if len(old) != 1 or len(remaining) != 1:
                raise ValueError(
                    f"{year}: ambiguous correction for CCN {ccn}; manual mapping required"
                )
            pairs.append((old.pop(), remaining.pop()))
        additions.extend(remaining)

    matched = set()
    changed = reappeared = 0
    for previous, new in pairs:
        row, observation = records[previous], observations[new]
        matched.add(previous)
        reappeared += row["present_in_latest_source"] == "false"
        if signature(row, business) != signature(observation, business):
            archived.append({**row, "superseded_on": on})
            row["version"] = str(int(row["version"]) + 1)
            row["version_first_seen_on"] = on
            row["version_last_seen_on"] = ""
            changed += 1
        row.update(observation)
        if on:
            row["first_seen_on"] = row["first_seen_on"] or on
            row["last_seen_on"] = on
            row["version_first_seen_on"] = row["version_first_seen_on"] or on
            row["version_last_seen_on"] = on
        row["present_in_latest_source"] = "true"
    for index, row in enumerate(records):
        if index not in matched:
            row["present_in_latest_source"] = "false"
    for index in additions:
        row = new_record(observations[index])
        row.update(first_seen_on=on, last_seen_on=on, version_first_seen_on=on,
                   version_last_seen_on=on, present_in_latest_source="true")
        records.append(row)
    current = pd.DataFrame(records, columns=columns + META).sort_values("record_id")
    versions = pd.DataFrame(archived, columns=columns + META + ["superseded_on"])
    if not versions.empty:
        versions = versions.sort_values(
            ["record_id", "version"],
            key=lambda s: pd.to_numeric(s) if s.name == "version" else s,
        )
    stats = {
        "source_rows": len(observed), "retained_rows": len(current),
        "absent_rows": int(current.present_in_latest_source.eq("false").sum()),
        "added": len(additions), "revised": changed, "reappeared": int(reappeared),
        "archived_versions": len(versions),
    }
    return current.reset_index(drop=True), versions.reset_index(drop=True), stats


def load_annual(raw_files, current_files):
    """One current version per retained occurrence; archived versions are excluded."""
    frames = []
    for year in sorted(raw_files):
        path = current_files.get(year, raw_files[year])
        frame = pd.read_csv(path, dtype=str, keep_default_na=False)
        for column in META:
            if column not in frame:
                frame[column] = ""  # An unobserved year has no invented presence/dates.
        frames.append(frame)
    return pd.concat(frames, ignore_index=True)

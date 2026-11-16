"""Offline batch auditing and production-pipeline replay."""

import hashlib
import json

import pandas as pd
import pytest

from scripts import audit_incidents as audit
from scripts import refresh_incidents as refresh


def table(year, entries):
    records = []
    for index, (ccn, ward) in enumerate(entries, 1):
        row = dict.fromkeys(refresh.COLUMNS, "")
        row.update(CCN=ccn, WARD=ward, OFFENSE="THEFT", METHOD="OTHERS", BLOCK="A",
                   OBJECTID=str(index), REPORT_DAT=f"{year}-06-01T12:00:00Z",
                   START_DATE=f"{year}-06-01T12:00:00Z")
        records.append(row)
    return pd.DataFrame(records, columns=refresh.COLUMNS)


def cache_year(cache, year, frame):
    cache.mkdir(exist_ok=True)
    path = cache / f"Crime_Incidents_in_{year}.csv"
    frame.to_csv(path, index=False)
    manifest = {"layers": {str(year): 40}, "exports": {str(year): {
        "source": f"{refresh.SERVICE}/40", "rows": len(frame),
        "retrieved_at": "2026-11-15T20:00:00+00:00",
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }}}
    audit.write_json(cache / "manifest.json", manifest)


def test_batch_audit_collects_all_ambiguous_groups(tmp_path):
    root, cache = tmp_path / "root", tmp_path / "cache"
    (root / "data/raw").mkdir(parents=True)
    table(2014, [("14000001", "1"), ("14000002", "1")]).to_csv(
        root / "data/raw/Crime_Incidents_in_2014.csv", index=False,
    )
    cache_year(cache, 2014, table(2014, [
        ("14000001", "2"), ("14000001", "3"), ("14000002", "2"), ("14000002", "3"),
    ]))
    assert not audit.audit(root, cache)
    report = json.loads((cache / "audit.json").read_text())
    assert {item["ccn"] for item in report["issues"]} == {"14000001", "14000002"}
    assert report["years"][0]["issues"] == 2


def test_altered_cached_file_is_rejected(tmp_path):
    cache_year(tmp_path, 2014, table(2014, [("14000001", "1")]))
    (tmp_path / "Crime_Incidents_in_2014.csv").write_text("partial")
    with pytest.raises(ValueError, match="altered frozen export"):
        audit.frozen(tmp_path)


def test_capture_resumes_after_a_failed_year(tmp_path, monkeypatch):
    monkeypatch.setattr(refresh, "discover", lambda: {2014: 40, 2015: 27})
    attempts = []

    def download(year, layer):
        attempts.append(year)
        if year == 2015 and attempts.count(2015) == 1:
            raise ValueError("temporary source error")
        return table(year, [(f"{str(year)[2:]}000001", "1")])

    monkeypatch.setattr(refresh, "download", download)
    assert not audit.capture(tmp_path)
    assert audit.capture(tmp_path)
    assert attempts.count(2014) == 1
    assert attempts.count(2015) == 2
    _, layers = audit.frozen(tmp_path)
    assert set(layers) == {2014, 2015}


def test_offline_replay_uses_real_refresh_without_touching_accepted_data(tmp_path):
    root, cache = tmp_path / "root", tmp_path / "cache"
    raw = root / "data/raw/Crime_Incidents_in_2014.csv"
    raw.parent.mkdir(parents=True)
    table(2014, [("14000001", "1"), ("14000002", "2")]).to_csv(raw, index=False)
    before = raw.read_bytes()
    cache_year(cache, 2014, table(2014, [("14000001", "1")]))
    audit.replay(root, cache)
    current = refresh.read_csv(cache / "replay/data/history/incidents/2014/current.csv.gz")
    assert len(current) == 2
    assert current.present_in_latest_source.eq("false").sum() == 1
    assert raw.read_bytes() == before
    assert not (root / "data/history").exists()
    assert (cache / "replay-pr.md").exists()
    audit.replay(root, cache, verify=True)
    verified = json.loads((cache / "replay-verification.json").read_text())
    assert verified["changed_files"] == []
    assert verified["verified_totals"]["retained_rows"] == 2
    with pytest.raises(ValueError, match="already exists"):
        audit.replay(root, cache)


def store_history(root, baseline, observed):
    from scripts.etl.incident_history import reconcile

    current, versions, _ = reconcile(2014, baseline, observed, on="2026-11-15")
    folder = root / "data/history/incidents/2014"
    folder.mkdir(parents=True)
    current.to_csv(folder / "current.csv.gz", index=False)
    versions.to_csv(folder / "versions.csv.gz", index=False)
    return current


def test_audit_detects_ambiguity_for_a_retained_record_missing_from_raw(tmp_path):
    from scripts.etl.incident_history import reconcile

    root, cache = tmp_path / "root", tmp_path / "cache"
    (root / "data/raw").mkdir(parents=True)
    legacy = table(2014, [("14000001", "1"), ("14000002", "1")])
    raw = legacy.iloc[1:]
    raw.to_csv(root / "data/raw/Crime_Incidents_in_2014.csv", index=False)
    current = store_history(root, legacy, raw)
    incoming = table(2014, [("14000001", "2"), ("14000001", "3"), ("14000002", "1")])
    cache_year(cache, 2014, incoming)
    with pytest.raises(ValueError, match="ambiguous correction"):
        reconcile(2014, raw, incoming, current=current, on="2026-11-16")
    assert not audit.audit(root, cache)
    report = json.loads((cache / "audit.json").read_text())
    assert [item["ccn"] for item in report["issues"]] == ["14000001"]
    assert report["issues"][0]["accepted"][0]["present_in_latest_source"] == "false"


@pytest.mark.parametrize("inventory", [{2014: 99}, {2014: 40, 2015: 27}])
def test_capture_does_not_replace_frozen_files_when_inventory_changes(
    tmp_path, monkeypatch, inventory,
):
    cache_year(tmp_path, 2014, table(2014, [("14000001", "1")]))
    manifest = (tmp_path / "manifest.json").read_bytes()
    raw = (tmp_path / "Crime_Incidents_in_2014.csv").read_bytes()
    monkeypatch.setattr(refresh, "discover", lambda: inventory)
    downloads = []

    def changed_download(year, layer):
        downloads.append(year)
        return table(year, [(f"{str(year)[2:]}000001", "2")])

    monkeypatch.setattr(refresh, "download", changed_download)
    with pytest.raises(ValueError, match="inventory changed"):
        audit.capture(tmp_path)
    assert downloads == []
    assert (tmp_path / "manifest.json").read_bytes() == manifest
    assert (tmp_path / "Crime_Incidents_in_2014.csv").read_bytes() == raw


@pytest.mark.parametrize("has_history", [False, True])
def test_replay_rejects_lost_occurrence_even_when_counts_are_unchanged(
    tmp_path, monkeypatch, has_history,
):
    root, cache = tmp_path / "root", tmp_path / "cache"
    (root / "data/raw").mkdir(parents=True)
    # Initial import has duplicate accepted occurrences; the history case has
    # a retained occurrence missing from accepted raw data altogether.
    legacy = table(2014, [("14000001", "1"), ("14000001", "1")])
    observed = table(2014, [("14000002", "2")])
    if has_history:
        legacy = table(2014, [("14000001", "1"), ("14000002", "2")])
        store_history(root, legacy, observed)
    accepted_raw = observed if has_history else legacy
    accepted_raw.to_csv(root / "data/raw/Crime_Incidents_in_2014.csv", index=False)
    cache_year(cache, 2014, observed)
    actual_refresh = refresh.refresh

    def losing_refresh(sandbox, **kwargs):
        result = actual_refresh(sandbox, **kwargs)
        path = sandbox / "data/history/incidents/2014/current.csv.gz"
        current = refresh.read_csv(path)
        index = current.index[current.CCN == "14000001"][0]
        previous_id = current.loc[index, "record_id"]
        current.loc[index, "record_id"] = "replacement-id"
        current.loc[index, "CCN"] = "14000003"
        current.to_csv(path, index=False)
        path = sandbox / "data/clean/incident_data.csv.gz"
        clean = refresh.read_csv(path)
        clean.loc[clean.record_id == previous_id, "ccn"] = "14000003"
        clean.loc[clean.record_id == previous_id, "record_id"] = "replacement-id"
        clean.to_csv(path, index=False)
        return result

    monkeypatch.setattr(refresh, "refresh", losing_refresh)
    with pytest.raises(ValueError, match="lost accepted"):
        audit.replay(root, cache)


def test_repeated_versions_cannot_cover_a_missing_duplicate_occurrence(tmp_path):
    old = table(2014, [("14000001", "1"), ("14000001", "1")])
    raw = tmp_path / "data/raw/Crime_Incidents_in_2014.csv"
    raw.parent.mkdir(parents=True)
    old.to_csv(raw, index=False)
    expected = audit.retention_expectation(tmp_path, 2014)
    current = table(2014, [("14000002", "2")])
    current["record_id"] = "new-record"
    versions = old.copy()
    versions["record_id"] = "one-occurrence-with-two-versions"
    with pytest.raises(ValueError, match="lost accepted raw occurrences"):
        audit.verify_retention(2014, current, versions, expected)


def test_capture_does_not_replace_a_corrupted_completed_snapshot(tmp_path, monkeypatch):
    cache_year(tmp_path, 2014, table(2014, [("14000001", "1")]))
    path = tmp_path / "Crime_Incidents_in_2014.csv"
    path.write_text("damaged snapshot")
    monkeypatch.setattr(refresh, "discover", lambda: {2014: 40})

    downloads = []

    def forbidden_download(*args):
        downloads.append(args)
        raise AssertionError("must not replace an already captured snapshot")

    monkeypatch.setattr(refresh, "download", forbidden_download)
    assert not audit.capture(tmp_path)
    assert path.read_text() == "damaged snapshot"
    assert downloads == []


def test_different_accepted_occurrences_cannot_share_one_versioned_record(tmp_path):
    old = table(2014, [("14000001", "1"), ("14000001", "2")])
    raw = tmp_path / "data/raw/Crime_Incidents_in_2014.csv"
    raw.parent.mkdir(parents=True)
    old.to_csv(raw, index=False)
    expected = audit.retention_expectation(tmp_path, 2014)
    current = table(2014, [("14000002", "3")])
    current["record_id"] = "new-record"
    versions = old.copy()
    versions["record_id"] = "one-occurrence-with-different-versions"
    with pytest.raises(ValueError, match="lost accepted raw occurrences"):
        audit.verify_retention(2014, current, versions, expected)


def test_retention_accepts_converged_payloads_with_distinct_history_ids(tmp_path):
    old = table(2014, [("14000001", "1"), ("14000001", "2")])
    raw = tmp_path / "data/raw/Crime_Incidents_in_2014.csv"
    raw.parent.mkdir(parents=True)
    old.to_csv(raw, index=False)
    versions = old.copy()
    versions["record_id"] = ["record-a", "record-b"]
    current = old.copy()
    current["WARD"] = "1"
    current["record_id"] = ["record-a", "record-b"]
    audit.verify_retention(2014, current, versions, audit.retention_expectation(tmp_path, 2014))

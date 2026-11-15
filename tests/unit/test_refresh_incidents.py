"""Offline tests of the real download/validation/staging boundary."""

from datetime import datetime
from zoneinfo import ZoneInfo

import pandas as pd
import pytest

from scripts import refresh_incidents as refresh

NOW = datetime(2026, 11, 15, 9, tzinfo=ZoneInfo("America/New_York"))


def source(years=(2025, 2026), *, broken=None, count=1):
    """A small ArcGIS service with real field/date/feature response shapes."""
    layers = {y: i + 10 for i, y in enumerate(years)}
    calls = []

    def fetch(url, **params):
        calls.append((url, params))
        if url == refresh.SERVICE:
            return {"layers": [{"name": f"Crime Incidents - {y}", "id": i}
                               for y, i in layers.items()]}
        year = next(y for y, i in layers.items() if f"/{i}" in url)
        if not url.endswith("/query"):
            return {
                "objectIdField": "OBJECTID", "maxRecordCount": 1,
                "fields": [{"name": c, "type": "esriFieldTypeDate" if c in refresh.DATES
                            else "esriFieldTypeString"} for c in refresh.COLUMNS[2:]],
            }
        if params.get("returnIdsOnly"):
            return {"objectIds": list(range(1, count + 1))}
        if broken == year:
            return {"features": []}
        ids = list(map(int, params["objectIds"].split(",")))
        rows = []
        for oid in ids:
            row = dict.fromkeys(refresh.COLUMNS[2:], "")
            stamp = int(pd.Timestamp(f"{year}-06-01T12:00Z").timestamp() * 1000)
            row.update(OBJECTID=oid, CCN="00123456", OFFENSE="THEFT", REPORT_DAT=stamp,
                       START_DATE=stamp, END_DATE=None)
            rows.append({"attributes": row, "geometry": {"x": 1, "y": 2}})
        return {"features": rows}

    return fetch, calls


def accepted(root, years=(2025,), count=1):
    raw = root / "data/raw"
    raw.mkdir(parents=True)
    fetch, _ = source(years, count=count)
    for year in years:
        refresh.download(year, 10 + years.index(year), fetch).to_csv(
            raw / f"Crime_Incidents_in_{year}.csv", index=False,
        )
    return raw


def test_full_export_batches_preserves_ccn_and_allows_repeated_ccn():
    fetch, calls = source(count=3)
    df = refresh.download(2026, 11, fetch)
    refresh.validate(df, 2026)
    assert list(df.OBJECTID) == [1, 2, 3]
    assert set(df.CCN) == {"00123456"}  # CCN is not the row identifier.
    assert len([p for _, p in calls if "objectIds" in p]) == 3


def test_download_rejects_truncation():
    fetch, _ = source(broken=2026)
    with pytest.raises(ValueError, match="incomplete"):
        refresh.download(2026, 11, fetch)


def test_download_rejects_source_mutation():
    fetch, _ = source()
    attempts = 0

    def changing(url, **params):
        nonlocal attempts
        result = fetch(url, **params)
        if params.get("returnIdsOnly"):
            attempts += 1
            if attempts == 2:
                result["objectIds"].append(2)
        return result

    with pytest.raises(ValueError, match="source changed"):
        refresh.download(2026, 11, changing)


@pytest.mark.parametrize("problem", ["duplicate", "missing", "wrong_year"])
def test_validation_rejects_suspicious_data(problem):
    fetch, _ = source(count=2)
    df = refresh.download(2026, 11, fetch)
    if problem == "duplicate":
        df.loc[1, "OBJECTID"] = df.loc[0, "OBJECTID"]
    elif problem == "missing":
        df = df.drop(columns="OFFENSE")
    else:
        df.loc[0, "REPORT_DAT"] = "2025-06-01T12:00:00Z"
    with pytest.raises(ValueError):
        refresh.validate(df, 2026)


def test_late_failure_leaves_every_file_and_marker_untouched(tmp_path):
    raw = accepted(tmp_path)
    before = {p.name: p.read_bytes() for p in raw.iterdir()}
    fetch, _ = source(broken=2026)
    marker = tmp_path / "marker"
    with pytest.raises(ValueError, match="incomplete"):
        refresh.refresh(tmp_path, fetch=fetch, marker=marker, now=NOW)
    assert before == {p.name: p.read_bytes() for p in raw.iterdir()}
    assert not marker.exists()
    assert not (tmp_path / "data/clean").exists()


def test_new_year_etl_then_identical_run_is_noop(tmp_path):
    accepted(tmp_path)
    fetch, _ = source()
    result = refresh.refresh(tmp_path, fetch=fetch, now=NOW)
    assert "data/raw/Crime_Incidents_in_2026.csv" in result["changed_files"]
    clean = tmp_path / "data/clean/incident_data.csv.gz"
    before = clean.read_bytes()
    assert len(pd.read_csv(clean)) == 2
    result = refresh.refresh(tmp_path, fetch=fetch, now=NOW)
    assert result["changed_files"] == []
    assert clean.read_bytes() == before


def test_monthly_fallback_and_daily_recent_selection(tmp_path):
    accepted(tmp_path, (2024, 2025))
    fetch, _ = source((2024, 2025, 2026))
    marker = tmp_path / "cache/month"
    result = refresh.refresh(tmp_path, fetch=fetch, marker=marker, now=NOW)
    assert [y["year"] for y in result["years"]] == [2024, 2025, 2026]
    assert result["historical_sweep"]
    result = refresh.refresh(tmp_path, fetch=fetch, marker=marker, now=NOW)
    assert [y["year"] for y in result["years"]] == [2025, 2026]
    marker.write_text("2026-10")
    assert refresh.refresh(tmp_path, fetch=fetch, marker=marker, now=NOW)["historical_sweep"]


def test_missing_existing_source_year_fails_closed(tmp_path):
    accepted(tmp_path, (2024, 2025))
    fetch, _ = source()
    with pytest.raises(ValueError, match="absent from source"):
        refresh.refresh(tmp_path, fetch=fetch, now=NOW)


def test_unpublished_current_year_is_visible(tmp_path):
    accepted(tmp_path)
    fetch, _ = source((2025,))
    result = refresh.refresh(tmp_path, fetch=fetch, now=NOW)
    assert "2026" in result["warnings"][0]


def test_pending_history_is_retained_but_counts_use_accepted_main(tmp_path):
    baseline = tmp_path / "accepted"
    candidate = tmp_path / "candidate"
    accepted(baseline, (2024, 2025), count=1)
    raw = accepted(candidate, (2024, 2025), count=2)
    pending_history = (raw / "Crime_Incidents_in_2024.csv").read_bytes()
    marker = tmp_path / "month"
    marker.write_text("2026-11")
    fetch, _ = source((2024, 2025, 2026), count=1)
    result = refresh.refresh(
        candidate, accepted_root=baseline, marker=marker, fetch=fetch, now=NOW,
    )
    assert not result["historical_sweep"]
    assert (raw / "Crime_Incidents_in_2024.csv").read_bytes() == pending_history
    assert len(pd.read_csv(candidate / "data/clean/incident_data.csv.gz")) == 4
    assert next(y for y in result["years"] if y["year"] == 2025)["previous_rows"] == 1


def test_decrease_retains_accepted_rows_in_separate_history(tmp_path):
    baseline = tmp_path / "accepted"
    candidate = tmp_path / "candidate"
    accepted(baseline, count=2)
    accepted(candidate, count=1)
    fetch, _ = source()
    refresh.refresh(candidate, accepted_root=baseline, fetch=fetch, now=NOW)
    history = refresh.read_csv(candidate / "data/history/incidents/2025/current.csv.gz")
    assert len(history) == 2
    assert history.present_in_latest_source.eq("false").sum() == 1
    assert len(refresh.read_csv(candidate / "data/raw/Crime_Incidents_in_2025.csv")) == 1
    assert len(pd.read_csv(candidate / "data/clean/incident_data.csv.gz")) == 3



def test_missing_incident_dates_are_allowed_but_invalid_dates_fail():
    fetch, _ = source()
    df = refresh.download(2026, 11, fetch)
    df.loc[0, "START_DATE"] = ""
    refresh.validate(df, 2026)
    df.loc[0, "START_DATE"] = "not-a-date"
    with pytest.raises(ValueError):
        refresh.validate(df, 2026)


def test_unchanged_daily_run_reports_entire_pending_diff(tmp_path):
    import hashlib

    baseline = tmp_path / "accepted"
    candidate = tmp_path / "candidate"
    accepted(baseline, (2024, 2025, 2026), count=1)
    raw = accepted(candidate, (2024, 2025, 2026), count=2)
    fetch, _ = source((2024, 2025, 2026), count=2)
    result = refresh.refresh(candidate, accepted_root=baseline, fetch=fetch, now=NOW)
    # First pass builds the fixture's missing cleaned output; the next is a true no-op.
    result = refresh.refresh(candidate, accepted_root=baseline, fetch=fetch, now=NOW)
    assert result["changed_files"] == []
    assert all(y["changed"] for y in result["years"])
    assert [y["year"] for y in result["pending_years"]] == [2024, 2025, 2026]
    historical = result["pending_years"][0]
    assert historical["previous_rows"] == 1
    assert historical["rows"] == 2
    assert historical["source"].endswith("/10")
    assert historical["sha256"] == hashlib.sha256(
        (raw / "Crime_Incidents_in_2024.csv").read_bytes()
    ).hexdigest()


def test_cli_separates_latest_run_from_pending_pr_details(tmp_path, monkeypatch):
    import sys

    baseline = tmp_path / "accepted"
    candidate = tmp_path / "candidate"
    accepted(baseline, (2024, 2025, 2026), count=1)
    accepted(candidate, (2024, 2025, 2026), count=2)
    fetch, _ = source((2024, 2025, 2026), count=2)
    result = refresh.refresh(candidate, accepted_root=baseline, fetch=fetch, now=NOW)
    summary = tmp_path / "summary.md"
    pr_body = tmp_path / "pr.md"
    monkeypatch.setattr(refresh, "refresh", lambda *args, **kwargs: result)
    monkeypatch.setattr(sys, "argv", [
        "refresh", "--summary", str(summary), "--pr-body", str(pr_body),
    ])
    refresh.main()
    assert "| 2024 |" not in summary.read_text()
    body = pr_body.read_text()
    for year in (2024, 2025, 2026):
        assert f"| {year} | 1 | 2 | True |" in body
    for item in result["pending_years"]:
        assert item["source"] in body
        assert item["sha256"] in body


def test_reverted_pending_year_is_excluded_from_pr_report(tmp_path):
    baseline = tmp_path / "accepted"
    candidate = tmp_path / "candidate"
    accepted(baseline, (2025, 2026), count=1)
    accepted(candidate, (2025, 2026), count=2)
    fetch, _ = source(count=1)
    result = refresh.refresh(candidate, accepted_root=baseline, fetch=fetch, now=NOW)
    assert result["changed_files"]  # Candidate changed back to accepted content.
    assert not any(y["changed"] for y in result["years"])
    assert result["pending_years"] == []
    assert all(not item["path"].startswith("data/raw/") for item in result["pending_files"])



def test_skipped_legacy_pending_year_retains_accepted_rows_without_invented_dates(tmp_path):
    baseline = tmp_path / "accepted"
    candidate = tmp_path / "candidate"
    accepted(baseline, (2024, 2025, 2026), count=2)
    accepted(candidate, (2024, 2025, 2026), count=1)
    fetch, _ = source((2024, 2025, 2026), count=2)
    refresh.refresh(candidate, accepted_root=baseline, fetch=fetch, now=NOW)
    history = refresh.read_csv(candidate / "data/history/incidents/2024/current.csv.gz")
    assert len(history) == 2
    assert history.present_in_latest_source.eq("false").sum() == 1
    assert history.first_seen_on.eq("").all()
    assert history.last_seen_on.eq("").all()



def test_merged_accepted_history_is_included_in_rebuilt_clean_output(tmp_path):
    baseline = tmp_path / "accepted"
    candidate = tmp_path / "candidate"
    accepted(baseline, (2024, 2025, 2026), count=1)
    raw = accepted(candidate, (2024, 2025, 2026), count=2)
    fetch, _ = source((2024, 2025, 2026), count=2)
    refresh.refresh(candidate, accepted_root=baseline, fetch=fetch, now=NOW)
    # A nonconflicting main-only historical correction has survived the merge.
    corrected = refresh.read_csv(raw / "Crime_Incidents_in_2024.csv")
    corrected.loc[0, "OFFENSE"] = "ACCEPTED CORRECTION"
    corrected.to_csv(raw / "Crime_Incidents_in_2024.csv", index=False)
    result = refresh.refresh(candidate, accepted_root=baseline, fetch=fetch, now=NOW)
    clean = pd.read_csv(candidate / "data/clean/incident_data.csv.gz")
    assert "ACCEPTED CORRECTION" in set(clean.offense)
    assert "data/clean/incident_data.csv.gz" in result["changed_files"]


def test_next_day_updates_observations_but_skipped_year_dates_stay_put(tmp_path):
    accepted(tmp_path, (2024, 2025, 2026))
    fetch, _ = source((2024, 2025, 2026))
    refresh.refresh(tmp_path, full_history=True, fetch=fetch, now=NOW)
    historical_path = tmp_path / "data/history/incidents/2024/current.csv.gz"
    historical = historical_path.read_bytes()
    raw = (tmp_path / "data/raw/Crime_Incidents_in_2025.csv").read_bytes()
    next_day = NOW.replace(day=16)
    result = refresh.refresh(tmp_path, fetch=fetch, now=next_day)
    assert historical_path.read_bytes() == historical
    latest = refresh.read_csv(tmp_path / "data/history/incidents/2025/current.csv.gz")
    assert set(latest.last_seen_on) == {"2026-11-16"}
    assert set(latest.first_seen_on) == {"2026-11-15"}
    assert (tmp_path / "data/raw/Crime_Incidents_in_2025.csv").read_bytes() == raw
    assert all("data/raw" not in p for p in result["changed_files"])


def test_failed_later_year_does_not_publish_observation_dates_or_versions(tmp_path):
    accepted(tmp_path, (2025, 2026))
    fetch, _ = source()
    refresh.refresh(tmp_path, fetch=fetch, now=NOW)
    before = {str(p.relative_to(tmp_path)): p.read_bytes()
              for p in (tmp_path / "data").rglob('*') if p.is_file()}
    fetch, _ = source(broken=2026)
    with pytest.raises(ValueError, match="incomplete"):
        refresh.refresh(tmp_path, fetch=fetch, now=NOW.replace(day=16))
    assert before == {str(p.relative_to(tmp_path)): p.read_bytes()
                      for p in (tmp_path / "data").rglob('*') if p.is_file()}


def test_regular_incident_etl_reads_retained_current_versions(tmp_path, monkeypatch):
    from scripts.etl.incidents import load_raw_annual

    accepted(tmp_path, (2025,), count=2)
    fetch, _ = source((2025,), count=1)
    refresh.refresh(tmp_path, fetch=fetch, now=NOW)
    monkeypatch.chdir(tmp_path)
    annual = load_raw_annual()
    assert len(annual) == 2
    assert annual.present_in_latest_source.eq("false").sum() == 1
    assert "superseded_on" not in annual.columns

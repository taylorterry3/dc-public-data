import pandas as pd
import pytest

from scripts.etl.incident_history import reconcile


def rows(*values):
    return pd.DataFrame([
        {"CCN": ccn, "OFFENSE": offense, "METHOD": "OTHERS", "REPORT_DAT": "2014-06-01T12:00:00Z",
         "START_DATE": "2014-06-01T12:00:00Z", "END_DATE": "", "BLOCK": "A",
         "OBJECTID": str(i), "X": "1.000000", "Y": "2.0", "OCTO_RECORD_ID": ""}
        for i, (ccn, offense) in enumerate(values, 1)
    ])


def test_disappearance_retains_record_with_unknown_legacy_dates():
    old = rows(("14000001", "THEFT"), ("14000002", "ROBBERY"))
    new = old.iloc[:1]
    current, versions, stats = reconcile(2014, old, new, on="2026-11-16")
    missing = current[current.CCN == "14000002"].iloc[0]
    assert missing.last_seen_on == missing.first_seen_on == ""
    assert missing.present_in_latest_source == "false"
    assert missing.baseline_imported_on == "2026-11-16"
    assert stats["absent_rows"] == 1
    assert len(current) == 2 and versions.empty


def test_correction_archives_previous_values_once_and_reappearance_keeps_id():
    old = rows(("14000001", "THEFT"), ("14000002", "ROBBERY"))
    current, versions, _ = reconcile(2014, old, old, on="2026-11-16")
    identity = current.loc[current.CCN == "14000001", "record_id"].iloc[0]
    revised = old.iloc[:1].copy()
    revised.loc[0, "OFFENSE"] = "BURGLARY"
    current, versions, _ = reconcile(2014, old, revised, current=current,
                                     versions=versions, on="2026-11-17")
    assert len(versions) == 1
    assert versions.iloc[0].OFFENSE == "THEFT"
    assert versions.iloc[0].version_last_seen_on == "2026-11-16"
    assert versions.iloc[0].superseded_on == "2026-11-17"
    assert current.loc[current.CCN == "14000001", "record_id"].iloc[0] == identity
    revised = pd.concat([revised, old.iloc[1:]], ignore_index=True)
    current, versions, stats = reconcile(2014, old, revised, current=current,
                                         versions=versions, on="2026-11-18")
    assert stats["reappeared"] == 1
    assert len(versions) == 1
    assert set(current.first_seen_on) == {"2026-11-16"}
    assert set(current.last_seen_on) == {"2026-11-18"}


def test_objectid_reload_does_not_change_identity_or_create_version():
    old = rows(("14000001", "THEFT"), ("14000001", "THEFT"))
    current, versions, _ = reconcile(2014, old, old, on="2026-11-16")
    new = old.copy()
    new["OBJECTID"] = ["100", "200"]
    new["X"] = "1"
    new["REPORT_DAT"] = "2014/06/01 12:00:00+00"
    latest, archive, _ = reconcile(2014, old, new, current=current,
                                  versions=versions, on="2026-11-17")
    assert set(current.record_id) == set(latest.record_id)
    assert archive.empty and len(latest) == 2


def test_ambiguous_multi_record_correction_fails():
    old = rows(("14000001", "THEFT"), ("14000001", "ROBBERY"))
    new = rows(("14000001", "HOMICIDE"), ("14000001", "BURGLARY"))
    with pytest.raises(ValueError, match="ambiguous correction"):
        reconcile(2014, old, new, on="2026-11-16")


def test_identical_same_day_observation_is_idempotent():
    old = rows(("14000001", "THEFT"))
    current, versions, _ = reconcile(2014, old, old, on="2026-11-16")
    again, archive, _ = reconcile(2014, old, old, current=current,
                                  versions=versions, on="2026-11-16")
    pd.testing.assert_frame_equal(current, again)
    pd.testing.assert_frame_equal(versions, archive)


def test_archive_preserves_original_payload_formatting():
    old = rows(("14000001", "THEFT"))
    old.loc[0, "REPORT_DAT"] = "2014/06/01 12:00:00+00"
    old.loc[0, "X"] = "1.234567890"
    current, versions, _ = reconcile(2014, old, old, on="2026-11-16")
    new = rows(("14000001", "ROBBERY"))
    _, versions, _ = reconcile(2014, old, new, current=current,
                               versions=versions, on="2026-11-17")
    assert versions.iloc[0].REPORT_DAT == "2014/06/01 12:00:00+00"
    assert versions.iloc[0].X == "1.234567890"


@pytest.mark.parametrize("reverse", [False, True])
def test_competing_incoming_anchor_revisions_fail_regardless_of_order(reverse):
    old = rows(("14000001", "THEFT"))
    old["WARD"] = "1"
    current, versions, _ = reconcile(2014, old, old, on="2026-11-16")
    incoming = rows(("14000001", "THEFT"), ("14000001", "THEFT"))
    incoming["WARD"] = ["2", "3"]
    if reverse:
        incoming = incoming.iloc[::-1].reset_index(drop=True)
    before = current.copy(deep=True)
    with pytest.raises(ValueError, match="ambiguous correction"):
        reconcile(2014, old, incoming, current=current, versions=versions, on="2026-11-17")
    pd.testing.assert_frame_equal(current, before)
    assert versions.empty


def test_equivalent_incoming_duplicates_still_preserve_multiplicity():
    old = rows(("14000001", "THEFT"))
    old["WARD"] = "1"
    current, versions, _ = reconcile(2014, old, old, on="2026-11-16")
    incoming = rows(("14000001", "THEFT"), ("14000001", "THEFT"))
    incoming["WARD"] = "2"
    latest, archive, stats = reconcile(2014, old, incoming, current=current,
                                       versions=versions, on="2026-11-17")
    assert len(latest) == 2
    assert set(current.record_id) < set(latest.record_id)
    assert stats["revised"] == stats["added"] == 1
    assert len(archive) == 1
    assert archive.iloc[0].WARD == "1"


@pytest.mark.parametrize("reverse", [False, True])
def test_block_whitespace_does_not_ambiguously_split_revised_duplicates(reverse):
    old = rows(("18067757", "SEX ABUSE"), ("18067757", "SEX ABUSE"))
    old["BLOCK"] = "500 - 699 BLOCK OF RANDOLPH STREET NW"
    old["LATITUDE"] = "38.9388072732"
    current, versions, _ = reconcile(2018, old, old, on="2026-11-15")
    incoming = old.copy()
    incoming["BLOCK"] = " 500  - 699 BLOCK OF RANDOLPH STREET NW "
    incoming["LATITUDE"] = "38.938803"
    incoming["OBJECTID"] = ["100", "200"]
    if reverse:
        incoming = incoming.iloc[::-1].reset_index(drop=True)
    latest, archive, stats = reconcile(2018, old, incoming, current=current,
                                       versions=versions, on="2026-11-16")
    assert set(latest.record_id) == set(current.record_id)
    assert stats["revised"] == 2
    assert stats["added"] == stats["absent_rows"] == 0
    assert len(archive) == 2
    assert set(archive.BLOCK) == set(old.BLOCK)
    assert set(latest.BLOCK) == set(incoming.BLOCK)


def test_whitespace_only_block_change_preserves_values_without_new_version():
    old = rows(("14000001", "THEFT"))
    old["BLOCK"] = "500 - 699 BLOCK OF RANDOLPH STREET NW"
    current, versions, _ = reconcile(2014, old, old, on="2026-11-15")
    incoming = old.copy()
    incoming["BLOCK"] = "500  - 699 BLOCK OF RANDOLPH STREET NW"
    latest, archive, stats = reconcile(2014, old, incoming, current=current,
                                       versions=versions, on="2026-11-16")
    assert archive.empty and stats["revised"] == 0
    assert set(latest.record_id) == set(current.record_id)
    assert latest.iloc[0].BLOCK == incoming.iloc[0].BLOCK

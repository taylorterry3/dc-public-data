import pytest


def test_years_completeness(arrest_data):
    """Test that the data includes all necessary years."""
    years = sorted(arrest_data.date.dt.year.unique())
    expected_years = list(range(2013, 2025))
    assert (
        years == expected_years
    ), f"Missing years. Expected {expected_years}, got {years}"


def test_wards_completeness(arrest_data):
    """Test that the data includes all necessary wards."""
    wards = sorted(arrest_data.WARD.unique())
    expected_wards = list(range(1, 9))
    assert (
        wards == expected_wards
    ), f"Missing wards. Expected {expected_wards}, got {wards}"


def test_no_missing_values(arrest_data):
    """Test that there are no missing values in key columns."""
    key_columns = ["date", "WARD", "category"]
    for col in key_columns:
        missing = arrest_data[col].isna().sum()
        assert missing == 0, f"Found {missing} missing values in {col}"

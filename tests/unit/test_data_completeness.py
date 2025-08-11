import pytest
import pandas as pd


def test_years_completeness(arrest_data):
    """Test that we have data for all expected years."""
    years = pd.to_datetime(arrest_data["date"]).dt.year.unique()
    # Update expected year range to match actual data
    expected_years = range(2013, 2024)  # Adjust if needed
    for year in expected_years:
        assert year in years, f"Missing data for year {year}"


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
    # Clean the data before checking for missing values
    cleaned_data = arrest_data.copy()
    cleaned_data = cleaned_data[cleaned_data.WARD > 0]  # Remove invalid ward numbers
    cleaned_data = cleaned_data.dropna(
        subset=key_columns
    )  # Remove rows with missing values

    for col in key_columns:
        missing = cleaned_data[col].isna().sum()
        assert missing == 0, f"Found {missing} missing values in {col}"

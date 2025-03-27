#!/usr/bin/env python

import pandas as pd
import numpy as np
from pathlib import Path
import re
from datetime import datetime
import shutil
import pytest
from generate_ward_reports import (
    generate_report,
    preprocess_data,
)


def get_project_root():
    """Get the project root directory."""
    return Path(__file__).parent.parent


def get_data_path(filename):
    """Get the full path to a data file."""
    return get_project_root() / "data" / "clean" / filename


def get_reports_path():
    """Get the full path to the reports directory."""
    return get_project_root() / "reports"


def test_data_completeness():
    """Test that the data includes all necessary years and wards."""
    print("\nTesting data completeness...")

    # Read the data
    arrest_data = pd.read_csv(get_data_path("arrest_data.csv.gz"), low_memory=False)
    arrest_data["date"] = pd.to_datetime(arrest_data["date"])

    # Check years
    years = sorted(arrest_data.date.dt.year.unique())
    expected_years = list(range(2013, 2025))
    assert (
        years == expected_years
    ), f"Missing years. Expected {expected_years}, got {years}"
    print("✓ Years check passed")

    # Check wards
    wards = sorted(arrest_data.WARD.unique())
    expected_wards = list(range(1, 9))
    assert (
        wards == expected_wards
    ), f"Missing wards. Expected {expected_wards}, got {wards}"
    print("✓ Wards check passed")

    # Check for missing values in key columns
    key_columns = ["date", "WARD"]
    for col in key_columns:
        missing = arrest_data[col].isna().sum()
        assert missing == 0, f"Found {missing} missing values in {col}"
    print("✓ No missing values in key columns")

    # Check category missing values
    missing_categories = arrest_data["category"].isna().sum()
    print(f"Note: Found {missing_categories} missing categories (this is expected)")


def create_test_data():
    """Create a small test dataset."""
    dates = pd.date_range(start="2023-01-01", end="2024-12-31", freq="D")
    n_records = len(dates) * 2  # 2 records per day

    data = {
        "date": np.repeat(dates, 2),
        "category": np.random.choice(
            ["Theft", "Narcotics", "Traffic Violations"], n_records
        ),
        "WARD": np.random.randint(1, 9, n_records),
        "ARREST_DISTRICT": np.random.choice(
            ["1D", "2D", "3D", "4D", "5D", "6D", "7D"], n_records
        ),
    }

    df = pd.DataFrame(data)
    return preprocess_data(df)


def create_test_officers_data():
    """Create test officers data."""
    return pd.DataFrame(
        {"year": [2021, 2022, 2023, 2024], "officers": [3500, 3400, 3300, 3200]}
    )


def test_report_sections():
    """Test that all required sections are present in the report."""
    df = create_test_data()
    officers_df = create_test_officers_data()

    report = generate_report(df, officers_df)

    # Check main sections
    required_sections = [
        "DC Metropolitan Police Department Adult Arrest Trends, 2023-2024",
        "Background",
        "Citywide Changes in Arrest Patterns",
        "Productivity per Officer",
        "Arrests by Category",
        "Appendix 1: Data by Ward",
        "Appendix 2: Data by Police District",
    ]

    for section in required_sections:
        assert section in report, f"Missing section: {section}"


def test_appendix_contents():
    """Test that ward and district appendices contain required elements."""
    df = create_test_data()
    officers_df = create_test_officers_data()

    report = generate_report(df, officers_df)

    # Check ward appendix
    for ward in range(1, 9):
        assert f"## Ward {ward}" in report
        assert "| Arrest Category | 2023 | 2024 | Change | % Change |" in report
        assert f"![](ward_{ward}_categories.png)" in report

    # Check district appendix
    for district in ["1D", "2D", "3D", "4D", "5D", "6D", "7D"]:
        assert f"## {district}" in report
        assert "| Arrest Category | 2023 | 2024 | Change | % Change |" in report
        assert f"![](district_{district}_categories.png)" in report


def test_plot_generation(tmp_path):
    """Test that plots are generated correctly."""
    df = create_test_data()
    officers_df = create_test_officers_data()

    # Create temporary directory for test plots
    reports_dir = tmp_path / "reports"
    reports_dir.mkdir()

    # Generate plots
    from generate_ward_reports import (
        generate_citywide_plots,
        generate_ward_plots,
        generate_district_plots,
    )

    # Generate citywide plots
    generate_citywide_plots(df, reports_dir, officers_df)
    assert (reports_dir / "citywide_categories.png").exists()
    assert (reports_dir / "citywide_officer_trends.png").exists()

    # Generate ward plots
    for ward in range(1, 9):
        generate_ward_plots(df, ward, reports_dir, officers_df)
        assert (reports_dir / f"ward_{ward}_categories.png").exists()

    # Generate district plots
    for district in ["1D", "2D", "3D", "4D", "5D", "6D", "7D"]:
        generate_district_plots(df, district, reports_dir, officers_df)
        assert (reports_dir / f"district_{district}_categories.png").exists()


def test_data_preprocessing():
    """Test that data preprocessing works correctly."""
    df = create_test_data()

    assert "year" in df.columns
    assert "month" in df.columns
    assert "month_year" in df.columns
    assert df["WARD"].min() > 0
    assert not df["WARD"].isna().any()
    assert not df["ARREST_DISTRICT"].isna().any()


def main():
    """Run all tests."""
    print("Starting ward report validation tests...")

    try:
        test_data_completeness()
        test_report_sections()
        test_appendix_contents()
        test_plot_generation()
        test_data_preprocessing()
        print("\nAll tests passed successfully!")
    except AssertionError as e:
        print(f"\n❌ Test failed: {str(e)}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())

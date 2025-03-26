#!/usr/bin/env python

import pandas as pd
import numpy as np
from pathlib import Path
import re
from datetime import datetime
import shutil
import pytest
from generate_ward_reports import (
    generate_ward_report,
    generate_citywide_report,
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
    }

    df = pd.DataFrame(data)
    return preprocess_data(df)


def create_test_officers_data():
    """Create test officers data."""
    return pd.DataFrame(
        {"year": [2021, 2022, 2023, 2024], "officers": [3500, 3400, 3300, 3200]}
    )


def test_report_generation():
    """Test basic report generation functionality."""
    df = create_test_data()
    officers_df = create_test_officers_data()

    # Generate a test ward report
    report = generate_ward_report(df, 1, officers_df)

    # Check for required sections
    assert "Citywide Changes in Arrest Patterns" in report
    assert "Ward 1 Overview" in report
    assert "Productivity per Officer" in report
    assert "Arrest Categories with Largest Increase 2023-2024" in report
    assert "Top Arrest Categories in 2024" in report
    assert "Arrests by Category, 2023-2024" in report


def test_date_range_coverage():
    """Test that reports cover the correct date range."""
    df = create_test_data()
    officers_df = create_test_officers_data()

    report = generate_ward_report(df, 1, officers_df)
    assert "2023-2024" in report  # Check date range in title
    assert "2024" in report  # Check current year
    assert "2023" in report  # Check previous year


def test_visualization_sections():
    """Test that visualization sections are properly formatted."""
    df = create_test_data()
    officers_df = create_test_officers_data()

    report = generate_ward_report(df, 1, officers_df)

    # Check for visualization references
    assert "![Arrests and Stops per Officer](citywide_officer_trends.png)" in report
    assert "![Arrests by category](ward_1_categories.png)" in report


def test_plot_generation(tmp_path):
    """Test that plots are generated correctly."""
    df = create_test_data()
    officers_df = create_test_officers_data()

    # Create temporary directory for test plots
    reports_dir = tmp_path / "reports"
    reports_dir.mkdir()

    # Generate plots
    from generate_ward_reports import generate_ward_plots, generate_citywide_plots

    generate_citywide_plots(df, reports_dir, officers_df)
    generate_ward_plots(df, 1, reports_dir, officers_df)

    # Check that plot files exist
    assert (reports_dir / "citywide_officer_trends.png").exists()
    assert (reports_dir / "ward_1_categories.png").exists()


def main():
    """Run all tests."""
    print("Starting ward report validation tests...")

    try:
        test_data_completeness()
        test_report_generation()
        test_date_range_coverage()
        test_visualization_sections()
        test_plot_generation()
        print("\nAll tests passed successfully!")
    except AssertionError as e:
        print(f"\n❌ Test failed: {str(e)}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())

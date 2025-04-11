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
import tempfile


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
    wards = sorted(arrest_data.ward.unique())
    expected_wards = list(range(1, 9))
    assert (
        wards == expected_wards
    ), f"Missing wards. Expected {expected_wards}, got {wards}"
    print("✓ Wards check passed")

    # Check for missing values in key columns
    key_columns = ["date", "ward"]
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
        "year": np.repeat(dates.year, 2),  # Add year column
        "category": np.random.choice(
            ["Theft", "Narcotics", "Traffic Violations"], n_records
        ),
        "ward": np.random.randint(1, 9, n_records),
        "arrest_district": np.random.choice(
            ["1D", "2D", "3D", "4D", "5D", "6D", "7D"], n_records
        ),
        "anc_id": np.random.choice(["1A", "2B", "3C", "4D"], n_records),  # Add ANC IDs
        "arrest_psa": np.random.choice(
            ["101", "102", "103", "104"], n_records
        ),  # Add PSA values
    }

    df = pd.DataFrame(data)
    return preprocess_data(df)


def create_test_officers_data():
    """Create test officers data."""
    return pd.DataFrame(
        {"year": [2021, 2022, 2023, 2024], "officers": [3500, 3400, 3300, 3200]}
    )


@pytest.fixture
def test_data():
    """Fixture for test data."""
    return create_test_data()


@pytest.fixture
def test_officers_data():
    """Fixture for test officers data."""
    return create_test_officers_data()


def test_report_sections(test_data, test_officers_data):
    """Test that all required sections are present in reports."""
    # Create a temporary directory for the report
    with tempfile.TemporaryDirectory() as temp_dir:
        reports_dir = Path(temp_dir)
        images_dir = reports_dir / "images"
        images_dir.mkdir(exist_ok=True)

        report = generate_report(test_data, test_officers_data, images_dir)

        required_sections = [
            "Background",
            "Citywide Changes in Arrest Patterns",
            "Productivity per Officer",
            "Arrests by Category",
            "Appendix 1: Data by Ward",
            "Appendix 2: Data by Police District",
        ]

        for section in required_sections:
            assert section in report, f"Missing section '{section}' in report"


def test_appendix_contents(test_data, test_officers_data):
    """Test that appendices contain the expected content."""
    # Create a temporary directory for the report
    with tempfile.TemporaryDirectory() as temp_dir:
        reports_dir = Path(temp_dir)
        images_dir = reports_dir / "images"
        images_dir.mkdir(exist_ok=True)

        report = generate_report(test_data, test_officers_data, images_dir)

        # Check ward appendix content
        assert "# Appendix 1: Data by Ward" in report
        for ward in range(1, 9):
            assert f"## Ward {ward}" in report
            assert "| Arrest Category | 2023 | 2024 | Change | % Change |" in report

        # Check district appendix content
        assert "# Appendix 2: Data by Police District" in report
        for district in ["1D", "2D", "3D", "4D", "5D", "6D", "7D"]:
            assert f"## {district}" in report
            assert "| Arrest Category | 2023 | 2024 | Change | % Change |" in report


def test_plot_generation(test_data, test_officers_data):
    """Test that plots are generated correctly."""
    # Create a temporary directory for the report
    with tempfile.TemporaryDirectory() as temp_dir:
        reports_dir = Path(temp_dir)
        images_dir = reports_dir / "images"
        images_dir.mkdir(exist_ok=True)

        # Generate citywide plots
        from generate_ward_reports import create_plots

        create_plots(test_data, reports_dir=reports_dir, officers_df=test_officers_data)

        # Generate ward plots
        for ward in range(1, 9):
            create_plots(test_data, "ward", ward, reports_dir, test_officers_data)

        # Generate district plots
        for district in ["1D", "2D", "3D", "4D", "5D", "6D", "7D"]:
            create_plots(
                test_data, "district", district, reports_dir, test_officers_data
            )

        # Check that the images directory exists
        assert images_dir.exists()

        # Check that the expected image files were created
        expected_images = [
            "citywide_categories.png",
            "citywide_officer_trends.png",
            "ward_1_categories.png",
            "ward_2_categories.png",
            "ward_3_categories.png",
            "ward_4_categories.png",
            "ward_5_categories.png",
            "ward_6_categories.png",
            "ward_7_categories.png",
            "ward_8_categories.png",
            "district_1D_categories.png",
            "district_2D_categories.png",
            "district_3D_categories.png",
            "district_4D_categories.png",
            "district_5D_categories.png",
            "district_6D_categories.png",
            "district_7D_categories.png",
        ]

        for image in expected_images:
            assert (images_dir / image).exists(), f"Missing image: {image}"


def test_data_preprocessing():
    """Test that data preprocessing works correctly."""
    df = create_test_data()

    assert "year" in df.columns
    assert "month" in df.columns
    assert "month_year" in df.columns
    assert df["ward"].min() > 0
    assert not df["ward"].isna().any()
    assert not df["arrest_district"].isna().any()


def main():
    """Run all tests."""
    print("Starting ward report validation tests...")

    try:
        test_data_completeness()
        test_report_sections(create_test_data(), create_test_officers_data())
        test_appendix_contents(create_test_data(), create_test_officers_data())
        test_plot_generation(create_test_data(), create_test_officers_data())
        test_data_preprocessing()
        print("\nAll tests passed successfully!")
    except AssertionError as e:
        print(f"\n❌ Test failed: {str(e)}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())

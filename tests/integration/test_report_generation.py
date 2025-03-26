import pytest
import re
from datetime import datetime
import pandas as pd
from pathlib import Path
from scripts.generate_ward_reports import (
    generate_ward_report,
    generate_citywide_report,
    preprocess_data,
    main,
)
import numpy as np


def test_reports_directory_exists(reports_dir):
    """Test that the reports directory exists."""
    assert reports_dir.exists(), "Reports directory not found"


def test_all_ward_reports_exist(reports_dir):
    """Test that reports exist for all wards."""
    for ward in range(1, 9):
        report_path = reports_dir / f"ward_{ward}_report.md"
        assert report_path.exists(), f"Missing report for Ward {ward}"


def test_report_sections(test_data, test_officers_data):
    """Test that all required sections are present in reports."""
    report = generate_ward_report(test_data, 1, test_officers_data)

    required_sections = [
        "Background",
        "Citywide Changes in Arrest Patterns",
        "Ward 1 Overview",
        "Productivity per Officer",
        "Arrest Categories with Largest Increase 2023-2024",
        "Top Arrest Categories in 2024",
        "Arrests by Category, 2023-2024",
    ]

    for section in required_sections:
        assert section in report, f"Missing section '{section}' in report"


def test_report_images(reports_dir):
    """Test that all required images exist."""
    for ward in range(1, 9):
        required_images = [
            f"ward_{ward}_monthly_trends.png",
            f"ward_{ward}_categories.png",
        ]
        for img in required_images:
            assert (
                reports_dir / img
            ).exists(), f"Missing image '{img}' for Ward {ward}"


def test_zero_arrest_filtering(reports_dir):
    """Test that categories with zero arrests are properly filtered."""
    for ward in range(1, 9):
        with open(reports_dir / f"ward_{ward}_report.md", "r") as f:
            content = f.read()

        # Extract tables
        tables = re.findall(r"\|.*\|", content)

        # Check percentage increase tables
        for table in tables:
            if "2023" in table and "2024" in table:
                # Extract numbers from table
                numbers = re.findall(r"\d+", table)
                if len(numbers) >= 4:  # At least 2 pairs of numbers
                    for i in range(0, len(numbers) - 2, 2):
                        count_2024 = int(numbers[i])
                        count_2023 = int(numbers[i + 1])
                        assert (
                            count_2024 > 0 and count_2023 > 0
                        ), f"Found zero arrests in Ward {ward} comparison table"


def test_date_range_coverage(arrest_data, reports_dir):
    """Test that the date range is covered by the data."""
    for ward in range(1, 9):
        ward_data = arrest_data[arrest_data.WARD == ward]
        assert not ward_data.empty, f"No data found for Ward {ward}"
        assert (
            ward_data.date.min().year <= 2024
        ), f"Data for Ward {ward} starts after 2024"
        assert (
            ward_data.date.max().year >= 2024
        ), f"Data for Ward {ward} ends before 2024"


def test_statistics_consistency(tmp_path, monkeypatch):
    """Test that statistics in reports are consistent."""
    # Create necessary directories
    data_dir = tmp_path / "data" / "clean"
    data_dir.mkdir(parents=True, exist_ok=True)

    # Create test data with known counts
    dates = pd.date_range("2023-01-01", "2024-12-31")
    n_records = len(dates)

    # Create structured test data with known counts
    arrest_data = pd.DataFrame(
        {
            "date": dates,
            "WARD": [1] * n_records,  # All records in Ward 1 for simplicity
            "category": ["Theft"] * n_records,  # Single category for simplicity
            "year": pd.DatetimeIndex(dates).year,
            "month": pd.DatetimeIndex(dates).month,
        }
    )

    officers_data = pd.DataFrame(
        {
            "year": range(2016, 2025),
            "officers": [3800] * 9,  # Consistent number for simplicity
        }
    )

    # Save test data
    arrest_data.to_csv(data_dir / "arrest_data.csv.gz", compression="gzip")
    officers_data.to_csv(data_dir / "officers.csv")

    # Run main function
    monkeypatch.chdir(tmp_path)
    main()

    # Read generated report
    with open(tmp_path / "reports" / "ward_1_report.md", "r") as f:
        report_content = f.read()

    # Calculate expected counts
    expected_2024_arrests = len(arrest_data[arrest_data.year == 2024])
    expected_2023_arrests = len(arrest_data[arrest_data.year == 2023])

    # Check for the exact format used in generate_ward_report
    expected_text = (
        f"In 2024 there were {expected_2024_arrests:,} adult arrests in Ward 1, a"
    )
    assert (
        expected_text in report_content
    ), f"2024 arrests mismatch in Ward 1 report. Expected {expected_2024_arrests}"

    # Print report content and expected values for debugging
    print("\nReport content:", report_content[:500])
    print(f"\nExpected 2024 arrests: {expected_2024_arrests}")
    print(f"Expected 2023 arrests: {expected_2023_arrests}")

    # Check the data directly
    print("\nData summary:")
    print(arrest_data.groupby("year").size())


def test_main_generates_all_reports(tmp_path, monkeypatch):
    """Test that main function generates all expected reports."""
    # Create necessary directories
    data_dir = tmp_path / "data" / "clean"
    data_dir.mkdir(parents=True, exist_ok=True)

    # Create and save test data
    arrest_data = pd.DataFrame(
        {
            "date": pd.date_range("2013-01-01", "2024-12-31"),
            "WARD": np.random.randint(1, 9, 4383),  # 12 years of daily data
            "category": np.random.choice(["Theft", "Assault"], 4383),
        }
    )

    officers_data = pd.DataFrame(
        {"year": range(2013, 2025), "officers": [3800] * 12}  # Dummy data
    )

    # Save test data
    arrest_data.to_csv(data_dir / "arrest_data.csv.gz", compression="gzip")
    officers_data.to_csv(data_dir / "officers.csv")

    # Run main function
    monkeypatch.chdir(tmp_path)
    main()

    # Check outputs
    reports_dir = tmp_path / "reports"
    assert reports_dir.exists()
    assert (reports_dir / "citywide_report.md").exists()

    # Check ward reports
    for ward in range(1, 9):
        ward_report = reports_dir / f"ward_{ward}_report.md"
        assert ward_report.exists()


@pytest.fixture
def test_data():
    """Create test data fixture."""
    dates = pd.date_range(start="2023-01-01", end="2024-12-31", freq="D")
    n_records = len(dates) * 2

    data = {
        "date": np.repeat(dates, 2),
        "category": np.random.choice(
            ["Theft", "Narcotics", "Traffic Violations"], n_records
        ),
        "WARD": np.random.randint(1, 9, n_records),
    }

    df = pd.DataFrame(data)
    return preprocess_data(df)


@pytest.fixture
def test_officers_data():
    """Create test officers data fixture."""
    return pd.DataFrame(
        {"year": [2021, 2022, 2023, 2024], "officers": [3500, 3400, 3300, 3200]}
    )

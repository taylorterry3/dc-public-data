#!/usr/bin/env python

import pandas as pd
import numpy as np
from pathlib import Path
import re
from datetime import datetime


def test_data_completeness():
    """Test that the data includes all necessary years and wards."""
    print("\nTesting data completeness...")

    # Read the data
    arrest_data = pd.read_csv("../data/clean/arrest_data.csv.gz", low_memory=False)
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
    key_columns = ["date", "WARD", "category"]
    for col in key_columns:
        missing = arrest_data[col].isna().sum()
        assert missing == 0, f"Found {missing} missing values in {col}"
    print("✓ No missing values in key columns")


def test_report_generation():
    """Test that reports were generated for all wards with correct content."""
    print("\nTesting report generation...")

    reports_dir = Path("../reports/wards")
    assert reports_dir.exists(), "Reports directory not found"

    # Check all ward reports exist
    for ward in range(1, 9):
        report_path = reports_dir / f"ward_{ward}_report.md"
        assert report_path.exists(), f"Missing report for Ward {ward}"

        # Read report content
        with open(report_path, "r") as f:
            content = f.read()

        # Check for required sections
        required_sections = [
            "Overview",
            "Top Arrest Categories in 2024",
            "Categories with Largest Percentage Increases from 2023",
            "Categories with Largest Percentage Increases (H2 vs H1 2024)",
            "Monthly Trends",
            "Category Distribution",
        ]
        for section in required_sections:
            assert (
                section in content
            ), f"Missing section '{section}' in Ward {ward} report"

        # Check for required images
        required_images = [
            f"ward_{ward}_monthly_trends.png",
            f"ward_{ward}_categories.png",
        ]
        for img in required_images:
            assert (
                reports_dir / img
            ).exists(), f"Missing image '{img}' for Ward {ward}"

    print("✓ All ward reports generated with required content")


def test_zero_arrest_filtering():
    """Test that categories with zero arrests are properly filtered."""
    print("\nTesting zero arrest filtering...")

    # Read the data
    arrest_data = pd.read_csv("../data/clean/arrest_data.csv.gz", low_memory=False)
    arrest_data["date"] = pd.to_datetime(arrest_data["date"])

    # Check each ward's report
    reports_dir = Path("../reports/wards")
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

    print("✓ Zero arrest filtering check passed")


def test_date_range_coverage():
    """Test that the date range is correctly covered in the reports."""
    print("\nTesting date range coverage...")

    # Read the data
    arrest_data = pd.read_csv("../data/clean/arrest_data.csv.gz", low_memory=False)
    arrest_data["date"] = pd.to_datetime(arrest_data["date"])

    # Check each ward's report
    reports_dir = Path("../reports/wards")
    for ward in range(1, 9):
        with open(reports_dir / f"ward_{ward}_report.md", "r") as f:
            content = f.read()

        # Extract date range from overview
        date_match = re.search(r"(\d{4}-\d{2}-\d{2}) to (\d{4}-\d{2}-\d{2})", content)
        assert date_match, f"Could not find date range in Ward {ward} report"

        start_date = datetime.strptime(date_match.group(1), "%Y-%m-%d")
        end_date = datetime.strptime(date_match.group(2), "%Y-%m-%d")

        # Check that the date range matches the data
        ward_data = arrest_data[arrest_data.WARD == ward]
        assert (
            start_date.date() == ward_data.date.min().date()
        ), f"Start date mismatch in Ward {ward} report"
        assert (
            end_date.date() == ward_data.date.max().date()
        ), f"End date mismatch in Ward {ward} report"

    print("✓ Date range coverage check passed")


def test_statistics_consistency():
    """Test that statistics in the reports are consistent with the data."""
    print("\nTesting statistics consistency...")

    # Read the data
    arrest_data = pd.read_csv("../data/clean/arrest_data.csv.gz", low_memory=False)
    arrest_data["date"] = pd.to_datetime(arrest_data["date"])

    # Check each ward's report
    reports_dir = Path("../reports/wards")
    for ward in range(1, 9):
        with open(reports_dir / f"ward_{ward}_report.md", "r") as f:
            content = f.read()

        # Extract total arrests from overview
        total_match = re.search(r"(\d+,?\d*) adult arrests", content)
        assert total_match, f"Could not find total arrests in Ward {ward} report"
        reported_total = int(total_match.group(1).replace(",", ""))

        # Calculate actual total
        ward_data = arrest_data[arrest_data.WARD == ward]
        actual_total = len(ward_data)

        assert (
            reported_total == actual_total
        ), f"Total arrests mismatch in Ward {ward} report. Expected {actual_total}, got {reported_total}"

    print("✓ Statistics consistency check passed")


def main():
    """Run all tests."""
    print("Starting ward report validation tests...")

    try:
        test_data_completeness()
        test_report_generation()
        test_zero_arrest_filtering()
        test_date_range_coverage()
        test_statistics_consistency()
        print("\nAll tests passed successfully!")
    except AssertionError as e:
        print(f"\n❌ Test failed: {str(e)}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())

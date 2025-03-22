import pytest
import re
from datetime import datetime


def test_reports_directory_exists(reports_dir):
    """Test that the reports directory exists."""
    assert reports_dir.exists(), "Reports directory not found"


def test_all_ward_reports_exist(reports_dir):
    """Test that reports exist for all wards."""
    for ward in range(1, 9):
        report_path = reports_dir / f"ward_{ward}_report.md"
        assert report_path.exists(), f"Missing report for Ward {ward}"


def test_report_sections(reports_dir):
    """Test that all reports have required sections."""
    required_sections = [
        "Overview",
        "Top Arrest Categories in 2024",
        "Arrest Categories with Largest Increase 2023-2024",
        "Arrest Categories with Largest Increase H1-H2 2024",
        "Monthly Trends",
        "Arrests by Category, 2023-2024",
    ]

    for ward in range(1, 9):
        with open(reports_dir / f"ward_{ward}_report.md", "r") as f:
            content = f.read()

        for section in required_sections:
            assert (
                section in content
            ), f"Missing section '{section}' in Ward {ward} report"


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


def test_statistics_consistency(arrest_data, reports_dir):
    """Test that statistics in the reports are consistent with the data."""
    for ward in range(1, 9):
        with open(reports_dir / f"ward_{ward}_report.md", "r") as f:
            content = f.read()

        # Extract 2024 arrests from overview
        arrests_2024_match = re.search(
            r"In 2024 there were (\d+,?\d*) adult arrests", content
        )
        assert arrests_2024_match, f"Could not find 2024 arrests in Ward {ward} report"
        reported_2024 = int(arrests_2024_match.group(1).replace(",", ""))

        # Calculate actual 2024 total
        ward_data = arrest_data[arrest_data.WARD == ward]
        actual_2024 = len(ward_data[ward_data.date.dt.year == 2024])

        assert (
            reported_2024 == actual_2024
        ), f"2024 arrests mismatch in Ward {ward} report. Expected {actual_2024}, got {reported_2024}"

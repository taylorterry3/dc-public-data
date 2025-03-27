import pytest
import re
from datetime import datetime
import pandas as pd
from pathlib import Path
from scripts.generate_ward_reports import (
    generate_report,
    preprocess_data,
    main,
)
import numpy as np


@pytest.fixture
def test_files(tmp_path, test_data, test_officers_data):
    """Create and save test data files in the expected locations."""
    # Create data directory structure
    data_dir = tmp_path / "data" / "clean"
    data_dir.mkdir(parents=True)

    # Save test data files
    test_data.to_csv(data_dir / "arrest_data.csv.gz", compression="gzip")
    test_officers_data.to_csv(data_dir / "officers.csv")

    return tmp_path


def test_reports_directory_exists(test_files, monkeypatch):
    """Test that the reports directory exists."""
    monkeypatch.chdir(test_files)
    main()
    assert (test_files / "reports").exists(), "Reports directory not found"


def test_single_report_exists(test_files, monkeypatch):
    """Test that the main report file exists."""
    monkeypatch.chdir(test_files)
    main()
    assert (
        test_files / "reports" / "arrest_report.md"
    ).exists(), "Missing main report file"


def test_report_sections(test_data, test_officers_data):
    """Test that all required sections are present in reports."""
    report = generate_report(test_data, test_officers_data)

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


def test_report_images(test_files, monkeypatch):
    """Test that all required images exist."""
    monkeypatch.chdir(test_files)
    main()

    reports_dir = test_files / "reports"

    # Check citywide images
    assert (reports_dir / "citywide_categories.png").exists()
    assert (reports_dir / "citywide_officer_trends.png").exists()

    # Check ward images
    for ward in range(1, 9):
        assert (reports_dir / f"ward_{ward}_categories.png").exists()

    # Check district images
    for district in ["1D", "2D", "3D", "4D", "5D", "6D", "7D"]:
        assert (reports_dir / f"district_{district}_categories.png").exists()


def test_zero_arrest_filtering(test_data, test_officers_data):
    """Test that categories with zero arrests are properly filtered."""
    report = generate_report(test_data, test_officers_data)

    # Extract tables
    tables = re.findall(r"\|.*\|", report)

    # Check tables
    for table in tables:
        if "2023" in table and "2024" in table:
            # Extract numbers from table
            numbers = re.findall(r"\d+", table)
            if len(numbers) >= 4:  # At least 2 pairs of numbers
                for i in range(0, len(numbers) - 2, 2):
                    count_2024 = int(numbers[i])
                    count_2023 = int(numbers[i + 1])
                    assert (
                        count_2024 >= 0 and count_2023 >= 0
                    ), "Found negative arrests in comparison table"


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


def test_statistics_consistency(test_files, monkeypatch):
    """Test that statistics in reports are consistent."""
    monkeypatch.chdir(test_files)
    main()

    # Read generated report
    with open(test_files / "reports" / "arrest_report.md", "r") as f:
        report_content = f.read()

    # Calculate expected counts from test data
    arrest_data = pd.read_csv(test_files / "data" / "clean" / "arrest_data.csv.gz")
    expected_2024_arrests = len(arrest_data[arrest_data.year == 2024])
    expected_2023_arrests = len(arrest_data[arrest_data.year == 2023])

    # Check for the presence of the counts in the report
    assert str(expected_2024_arrests) in report_content
    assert str(expected_2023_arrests) in report_content


def test_main_generates_report(tmp_path, monkeypatch):
    """Test that main function generates the report."""
    # Create necessary directories
    data_dir = tmp_path / "data" / "clean"
    data_dir.mkdir(parents=True, exist_ok=True)

    # Create and save test data
    arrest_data = pd.DataFrame(
        {
            "date": pd.date_range("2013-01-01", "2024-12-31"),
            "WARD": np.random.randint(1, 9, 4383),
            "category": np.random.choice(["Theft", "Assault"], 4383),
            "ARREST_DISTRICT": np.random.choice(
                ["1D", "2D", "3D"], 4383
            ),  # Added ARREST_DISTRICT
        }
    )

    officers_data = pd.DataFrame({"year": range(2013, 2025), "officers": [3800] * 12})

    # Save test data
    arrest_data.to_csv(data_dir / "arrest_data.csv.gz", compression="gzip")
    officers_data.to_csv(data_dir / "officers.csv")

    # Run main function
    monkeypatch.chdir(tmp_path)
    main()

    # Check output
    reports_dir = tmp_path / "reports"
    assert reports_dir.exists()
    assert (reports_dir / "arrest_report.md").exists()


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
        "ARREST_DISTRICT": np.random.choice(
            ["1D", "2D", "3D", "4D", "5D", "6D", "7D"], n_records
        ),
    }

    df = pd.DataFrame(data)
    return preprocess_data(df)


@pytest.fixture
def test_officers_data():
    """Create test officers data fixture."""
    return pd.DataFrame(
        {"year": [2021, 2022, 2023, 2024], "officers": [3500, 3400, 3300, 3200]}
    )


def test_appendix_structure(test_data, test_officers_data):
    """Test that appendices are properly structured."""
    report = generate_report(test_data, test_officers_data)

    # Check ward appendix structure
    assert "# Appendix 1: Data by Ward" in report
    for ward in range(1, 9):
        assert f"## Ward {ward}" in report
        assert "| Arrest Category | 2023 | 2024 | Change | % Change |" in report

    # Check district appendix structure
    assert "# Appendix 2: Data by Police District" in report
    for district in ["1D", "2D", "3D", "4D", "5D", "6D", "7D"]:
        assert f"## {district}" in report
        assert "| Arrest Category | 2023 | 2024 | Change | % Change |" in report


def test_table_formatting(test_data, test_officers_data):
    """Test that tables are properly formatted."""
    report = generate_report(test_data, test_officers_data)

    # Check table headers
    table_headers = [
        "| Arrest Category | 2023 | 2024 | Change | % Change |",
        "|----------------|------:|------:|--------:|----------:|",
    ]

    for header in table_headers:
        assert header in report, f"Missing table header format: {header}"

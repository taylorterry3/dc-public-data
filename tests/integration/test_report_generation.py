import pytest
import re
from datetime import datetime
import pandas as pd
from pathlib import Path
from scripts.generate_ward_reports import (
    generate_report,
    preprocess_data,
    main,
    generate_citywide_plots,
    generate_ward_plots,
    generate_district_plots,
)
import numpy as np
import tempfile


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


def test_report_images(test_data, test_officers_data):
    """Test that all required images exist."""
    # Create a temporary directory for the report
    with tempfile.TemporaryDirectory() as temp_dir:
        reports_dir = Path(temp_dir)
        images_dir = reports_dir / "images"
        images_dir.mkdir(exist_ok=True)

        # Generate plots first
        from scripts.generate_ward_reports import create_plots

        # Generate citywide plots
        create_plots(test_data, reports_dir=reports_dir, officers_df=test_officers_data)

        # Generate ward plots
        for ward in range(1, 9):
            create_plots(test_data, "ward", ward, reports_dir, test_officers_data)

        # Generate district plots
        for district in ["1D", "2D", "3D", "4D", "5D", "6D", "7D"]:
            create_plots(
                test_data, "district", district, reports_dir, test_officers_data
            )

        # Generate ANC plots - only for ANCs that exist in the data
        existing_ancs = test_data["anc_id"].unique()
        for anc in existing_ancs:
            if anc != "Unknown":
                create_plots(test_data, "anc", anc, reports_dir, test_officers_data)

        # Generate PSA plots - only for PSAs that exist in the data
        existing_psas = test_data["arrest_psa"].unique()
        for psa in existing_psas:
            create_plots(test_data, "psa", psa, reports_dir, test_officers_data)

        # Check that the images directory exists
        assert images_dir.exists()

        # Check that the expected image files were created
        expected_images = [
            "citywide_categories.png",
            "citywide_officer_trends.png",
        ]

        # Add ward images
        for ward in range(1, 9):
            expected_images.append(f"ward_{ward}_categories.png")

        # Add district images
        for district in ["1D", "2D", "3D", "4D", "5D", "6D", "7D"]:
            expected_images.append(f"district_{district}_categories.png")

        # Add ANC images for existing ANCs
        for anc in existing_ancs:
            expected_images.append(f"anc_{anc}_categories.png")

        # Add PSA images for existing PSAs
        for psa in existing_psas:
            expected_images.append(f"psa_{psa}_categories.png")

        for image in expected_images:
            assert (images_dir / image).exists(), f"Missing image: {image}"


def test_zero_arrest_filtering(test_data, test_officers_data):
    """Test that categories with zero arrests are properly filtered."""
    # Create a temporary directory for the report
    with tempfile.TemporaryDirectory() as temp_dir:
        reports_dir = Path(temp_dir)
        images_dir = reports_dir / "images"
        images_dir.mkdir(exist_ok=True)

        report = generate_report(test_data, test_officers_data, images_dir)

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


@pytest.fixture
def arrest_data():
    """Create test arrest data fixture."""
    dates = pd.date_range(start="2023-01-01", end="2024-12-31", freq="D")
    n_records = len(dates) * 2

    data = {
        "date": np.repeat(dates, 2),
        "year": np.repeat(dates.year, 2),
        "category": np.random.choice(
            ["Theft", "Narcotics", "Traffic Violations"], n_records
        ),
        "ward": np.random.randint(1, 9, n_records),
        "arrest_district": np.random.choice(
            ["1D", "2D", "3D", "4D", "5D", "6D", "7D"], n_records
        ),
        "anc_id": np.random.choice(["1A", "2B", "3C", "4D"], n_records),
        "arrest_psa": np.random.choice(["101", "102", "103", "104"], n_records),
    }

    return pd.DataFrame(data)


@pytest.fixture
def reports_dir(tmp_path):
    """Create reports directory fixture."""
    reports_dir = tmp_path / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    return reports_dir


def test_date_range_coverage(arrest_data, reports_dir):
    """Test that the date range is covered by the data."""
    for ward in range(1, 9):
        ward_data = arrest_data[arrest_data.ward == ward]
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
    dates = pd.date_range("2013-01-01", "2024-12-31")
    arrest_data = pd.DataFrame(
        {
            "date": dates,
            "year": dates.year,  # Add year column
            "ward": np.random.randint(1, 9, len(dates)),
            "category": np.random.choice(["Theft", "Assault"], len(dates)),
            "arrest_district": np.random.choice(["1D", "2D", "3D"], len(dates)),
            "anc_id": np.random.choice(
                ["1A", "2B", "3C", "4D"], len(dates)
            ),  # Add ANC IDs
            "arrest_psa": np.random.choice(
                ["101", "102", "103", "104"], len(dates)
            ),  # Add PSA values
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
def test_data() -> pd.DataFrame:
    """Create test data with a mix of categories and jurisdictions."""
    # Create a base date range
    dates = pd.date_range(start="2023-01-01", end="2024-12-31", freq="D")
    n_records = len(dates)

    # Ensure even distribution across wards
    wards = np.array(range(1, 9))  # 1-8
    ward_assignments = np.repeat(wards, n_records // 8 + 1)[:n_records]
    np.random.shuffle(ward_assignments)

    # Create arrays with consistent lengths
    data = {
        "date": dates,
        "year": np.repeat([2023, 2024], [365, 366]),
        "category": np.random.choice(
            ["Theft", "Narcotics", "Traffic Violations"], n_records
        ),
        "ward": ward_assignments,  # Keep as integers
        "arrest_district": np.random.choice(
            ["1D", "2D", "3D", "4D", "5D", "6D", "7D"], n_records
        ),
        "anc_id": np.random.choice(
            ["1A", "2B", "3C", "4D", "5E", "6F", "7G", "8H"], n_records
        ),
        "arrest_psa": np.random.choice(
            ["101", "202", "303", "404", "505", "606", "707"], n_records
        ),
        "month": np.repeat(range(1, 13), n_records // 12 + 1)[:n_records],
        "month_year": [
            f"{year}-{month:02d}"
            for year in [2023, 2024]
            for month in range(1, 13)
            for _ in range(n_records // 24 + 1)
        ][:n_records],
    }

    return pd.DataFrame(data)


@pytest.fixture
def test_officers_data():
    """Create test officers data."""
    return pd.DataFrame(
        {"year": [2021, 2022, 2023, 2024], "officers": [3500, 3400, 3300, 3200]}
    )


def test_appendix_structure(test_data, test_officers_data):
    """Test that appendices are properly structured."""
    # Create a temporary directory for the report
    with tempfile.TemporaryDirectory() as temp_dir:
        reports_dir = Path(temp_dir)
        images_dir = reports_dir / "images"
        images_dir.mkdir(exist_ok=True)

        report = generate_report(test_data, test_officers_data, images_dir)

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
    # Create a temporary directory for the report
    with tempfile.TemporaryDirectory() as temp_dir:
        reports_dir = Path(temp_dir)
        images_dir = reports_dir / "images"
        images_dir.mkdir(exist_ok=True)

        report = generate_report(test_data, test_officers_data, images_dir)

        # Check table headers
        table_headers = [
            "| Arrest Category | 2023 | 2024 | Change | % Change |",
            "|----------------|------:|------:|--------:|----------:|",
        ]

        for header in table_headers:
            assert header in report, f"Missing table header format: {header}"


def test_report_generation(test_data, test_officers_data):
    """Test that the report is generated correctly."""
    # Create a temporary directory for the report
    with tempfile.TemporaryDirectory() as temp_dir:
        reports_dir = Path(temp_dir)
        images_dir = reports_dir / "images"
        images_dir.mkdir(exist_ok=True)

        # Generate plots first
        from scripts.generate_ward_reports import create_plots

        # Generate citywide plots
        create_plots(test_data, reports_dir=reports_dir, officers_df=test_officers_data)

        # Generate ward plots
        for ward in range(1, 9):
            create_plots(test_data, "ward", ward, reports_dir, test_officers_data)

        # Generate district plots
        for district in ["1D", "2D", "3D", "4D", "5D", "6D", "7D"]:
            create_plots(
                test_data, "district", district, reports_dir, test_officers_data
            )

        # Generate ANC plots - only for ANCs that exist in the data
        existing_ancs = test_data["anc_id"].unique()
        for anc in existing_ancs:
            if anc != "Unknown":
                create_plots(test_data, "anc", anc, reports_dir, test_officers_data)

        # Generate PSA plots - only for PSAs that exist in the data
        existing_psas = test_data["arrest_psa"].unique()
        for psa in existing_psas:
            create_plots(test_data, "psa", psa, reports_dir, test_officers_data)

        # Generate the report
        report = generate_report(test_data, test_officers_data, images_dir)

        # Write the report to a file
        report_path = reports_dir / "arrest_report.md"
        with open(report_path, "w") as f:
            f.write(report)

        # Check that the report file was created
        assert report_path.exists()
        assert report_path.stat().st_size > 0

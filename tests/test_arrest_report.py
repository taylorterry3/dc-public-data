import re
from pathlib import Path


def test_ward_2_weapon_violations_2023():
    """Test that Ward 2 had 193 arrests for Weapon Violations in 2023."""
    report_path = Path("reports/arrest_report.md")
    assert report_path.exists(), "Report file not found"

    with open(report_path, "r") as f:
        content = f.read()

    # Find the Ward 2 section
    ward_2_section = re.search(r"## Ward 2\n\n(.*?)(?=## Ward 3)", content, re.DOTALL)
    assert ward_2_section, "Ward 2 section not found"

    # Find the Weapon Violations row
    weapon_row = re.search(r"\| Weapon Violations \| (\d+) \|", ward_2_section.group(1))
    assert weapon_row, "Weapon Violations row not found in Ward 2"

    assert (
        int(weapon_row.group(1)) == 193
    ), "Ward 2 Weapon Violations count for 2023 is incorrect"


def test_district_3d_weapon_violations_2023():
    """Test that District 3D had 203 arrests for Weapon Violations in 2023."""
    report_path = Path("reports/arrest_report.md")
    assert report_path.exists(), "Report file not found"

    with open(report_path, "r") as f:
        content = f.read()

    # Find the District 3D section
    district_3d_section = re.search(r"## 3D\n\n(.*?)(?=## 4D)", content, re.DOTALL)
    assert district_3d_section, "District 3D section not found"

    # Find the Weapon Violations row
    weapon_row = re.search(
        r"\| Weapon Violations \| (\d+) \|", district_3d_section.group(1)
    )
    assert weapon_row, "Weapon Violations row not found in District 3D"

    assert (
        int(weapon_row.group(1)) == 203
    ), "District 3D Weapon Violations count for 2023 is incorrect"


def test_anc_7b_liquor_law_violations_2024():
    """Test that ANC 7B had 29 arrests for Liquor Law Violations in 2024."""
    report_path = Path("reports/arrest_report.md")
    assert report_path.exists(), "Report file not found"

    with open(report_path, "r") as f:
        content = f.read()

    # Find the ANC 7B section
    anc_7b_section = re.search(r"## ANC 7B\n\n(.*?)(?=## ANC 7C)", content, re.DOTALL)
    assert anc_7b_section, "ANC 7B section not found"

    # Find the Liquor Law Violations row
    liquor_row = re.search(
        r"\| Liquor Law Violations \| \d+ \| (\d+) \|", anc_7b_section.group(1)
    )
    assert liquor_row, "Liquor Law Violations row not found in ANC 7B"

    assert (
        int(liquor_row.group(1)) == 29
    ), "ANC 7B Liquor Law Violations count for 2024 is incorrect"


def test_psa_407_traffic_violations_2024():
    """Test that PSA 407 had 41 arrests for Traffic Violations in 2024."""
    report_path = Path("reports/arrest_report.md")
    assert report_path.exists(), "Report file not found"

    with open(report_path, "r") as f:
        content = f.read()

    # Find the PSA 407 section
    psa_407_section = re.search(
        r"## PSA 407\n\n(.*?)(?=## PSA 408)", content, re.DOTALL
    )
    assert psa_407_section, "PSA 407 section not found"

    # Find the Traffic Violations row
    traffic_row = re.search(
        r"\| Traffic Violations \| \d+ \| (\d+) \|", psa_407_section.group(1)
    )
    assert traffic_row, "Traffic Violations row not found in PSA 407"

    assert (
        int(traffic_row.group(1)) == 41
    ), "PSA 407 Traffic Violations count for 2024 is incorrect"

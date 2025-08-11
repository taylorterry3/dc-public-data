import pytest
import pandas as pd
from pathlib import Path
import os
import sys
import numpy as np

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


@pytest.fixture
def data_dir():
    return Path(__file__).parent.parent / "data" / "clean"


@pytest.fixture
def arrest_data():
    """Fixture for test arrest data."""
    df = pd.DataFrame(
        {
            "date": pd.date_range("2013-01-01", "2024-12-31"),
            "WARD": np.random.randint(1, 9, 4383),
            "category": np.random.choice(["Theft", "Assault"], 4383),
        }
    )

    # Add the required columns that the main script creates
    df["date"] = pd.to_datetime(df["date"])
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["month_year"] = df["date"].dt.strftime("%Y-%m")

    return df


@pytest.fixture
def officers_data():
    """Fixture for test officers data."""
    return pd.DataFrame(
        {"year": range(2013, 2025), "officers": [3800] * 12}  # Dummy data
    )


@pytest.fixture
def arrest_data_path(data_dir):
    return data_dir / "arrest_data.csv.gz"


@pytest.fixture
def officers_data_path(data_dir):
    return data_dir / "officers.csv"


@pytest.fixture
def reports_dir():
    """Get the path to the reports directory."""
    return Path("reports")


@pytest.fixture
def sample_arrest_data():
    # Create sample data covering 2016-2024
    dates = pd.date_range("2016-01-01", "2024-12-31", freq="D")
    return pd.DataFrame(
        {
            "date": dates,
            "WARD": np.random.randint(1, 9, len(dates)),
            "category": np.random.choice(["Theft", "Assault", "DUI"], len(dates)),
        }
    )

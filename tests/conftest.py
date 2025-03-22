import pytest
import pandas as pd
from pathlib import Path


@pytest.fixture
def arrest_data():
    """Load arrest data for testing."""
    data = pd.read_csv("data/clean/arrest_data.csv.gz", low_memory=False)
    data["date"] = pd.to_datetime(data["date"])
    return data


@pytest.fixture
def reports_dir():
    """Get the path to the reports directory."""
    return Path("reports")

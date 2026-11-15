"""ETL pipeline for DC crime incident data."""

from pathlib import Path

import pandas as pd

from scripts.etl.common import data_cleanup
from scripts.etl.incident_history import load_annual

RAW_INCIDENTS_GLOB = "data/raw/Crime_Incidents*"
RAW_INCIDENTS_ALL = Path("data/raw/dc-crimes-search-results.csv")
CLEAN_INCIDENTS = Path("data/clean/incident_data.csv.gz")
CLEAN_INCIDENTS_ALL = Path("data/clean/incident_data_all.csv.gz")


def load_raw_annual() -> pd.DataFrame:
    """Load and concatenate annual Crime_Incidents_in_*.csv files."""
    files = {int(p.stem.rsplit("_", 1)[1]): p
             for p in Path("data/raw").glob("Crime_Incidents_in_*.csv")}
    current = {int(p.parent.name): p
               for p in Path("data/history/incidents").glob("*/current.csv.gz")}
    return load_annual(files, current)


def load_raw_all(path: Path = RAW_INCIDENTS_ALL) -> pd.DataFrame:
    """Load the broader dc-crimes-search-results dataset."""
    return pd.read_csv(path, low_memory=False)


def run(
    output_path: Path = CLEAN_INCIDENTS,
    output_all_path: Path = CLEAN_INCIDENTS_ALL,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Clean and save both incident datasets.

    Returns (incidents_df, incidents_all_df). Pass None for either output path to skip writing.
    """
    incidents = data_cleanup(load_raw_annual(), "START_DATE")
    incidents_all = data_cleanup(load_raw_all(), "START_DATE")

    print(f"Annual incident records: {len(incidents):,}")
    print(f"All-time incident records: {len(incidents_all):,}")

    if output_path is not None:
        incidents.to_csv(output_path, index=False, compression="gzip")
        print(f"Wrote {len(incidents):,} rows to {output_path}")

    if output_all_path is not None:
        incidents_all.to_csv(output_all_path, index=False, compression="gzip")
        print(f"Wrote {len(incidents_all):,} rows to {output_all_path}")

    return incidents, incidents_all


if __name__ == "__main__":
    run()

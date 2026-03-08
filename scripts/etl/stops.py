"""ETL pipeline for DC MPD stop data."""

import pandas as pd
from pathlib import Path

from scripts.etl.common import data_cleanup

RAW_STOPS_OLD = Path("data/raw/Stop_Data.csv.gz")
RAW_STOPS_2023_2025 = Path("data/raw/Stop_Data_2023-2025.csv.gz")
CLEAN_STOPS = Path("data/clean/stop_data.csv.gz")


def load_raw(old_path: Path = RAW_STOPS_OLD, new_path: Path = RAW_STOPS_2023_2025) -> pd.DataFrame:
    """Merge the two stop data files on their common columns."""
    old = pd.read_csv(old_path, low_memory=False)
    new = pd.read_csv(new_path, low_memory=False)
    common_cols = list(set(old.columns) & set(new.columns))
    return pd.concat([old[common_cols], new[common_cols]], ignore_index=True)


def run(
    old_path: Path = RAW_STOPS_OLD,
    new_path: Path = RAW_STOPS_2023_2025,
    output_path: Path = CLEAN_STOPS,
) -> pd.DataFrame:
    """Merge, clean, dedup, and save stop data.

    Returns the cleaned DataFrame. Pass output_path=None to skip writing.
    """
    df = load_raw(old_path, new_path)
    df = data_cleanup(df, "DATETIME")
    df = df.drop_duplicates(subset="ccn_anonymized")

    print(f"Stop records after dedup: {len(df):,}")

    if output_path is not None:
        df.to_csv(output_path, index=False, compression="gzip")
        print(f"Wrote {len(df):,} rows to {output_path}")

    return df


if __name__ == "__main__":
    run()

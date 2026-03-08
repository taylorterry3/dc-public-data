"""ETL pipeline for DC 311 city service requests."""

import glob
import numpy as np
import pandas as pd
from pathlib import Path

RAW_311_GLOB = "data/raw/311_City_Service_Requests*.csv.gz"
CLEAN_311_TEMPLATE = "data/clean/311_data_part_{}.csv.gz"
NUM_PARTS = 3


def load_raw() -> pd.DataFrame:
    """Load and concatenate all 311 raw CSV files."""
    files = glob.glob(RAW_311_GLOB)
    return pd.concat([pd.read_csv(f) for f in files], ignore_index=True)


def run(output_template: str = CLEAN_311_TEMPLATE, num_parts: int = NUM_PARTS) -> pd.DataFrame:
    """Load, concatenate, and split 311 data into parts.

    The data is split due to its size (~180 MB uncompressed).
    Returns the combined DataFrame. Pass output_template=None to skip writing.
    """
    df = load_raw()
    print(f"311 records: {len(df):,}")

    if output_template is not None:
        for idx, chunk in enumerate(np.array_split(df, num_parts)):
            path = output_template.format(idx)
            chunk.to_csv(path, index=False, compression="gzip")
            print(f"Wrote part {idx} ({len(chunk):,} rows) to {path}")

    return df


if __name__ == "__main__":
    run()

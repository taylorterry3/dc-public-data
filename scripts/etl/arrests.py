"""ETL pipeline for DC adult arrest data."""

import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from pathlib import Path

from scripts.etl.common import data_cleanup, arrest_category_cleanup

RAW_ARRESTS = Path("data/raw/Adult_Arrests.csv.gz")
RAW_ARRESTS_2025 = Path("data/raw/2025AdultArrests_OpenData.csv")
RAW_WARDS = Path("data/raw/Wards_from_2022.geojson")
RAW_SMD = Path("data/raw/Single_Member_District_from_2023.geojson")
CLEAN_ARRESTS = Path("data/clean/arrest_data.csv.gz")

# Column rename map for the newer annual file format (title case → UPPER_SNAKE_CASE)
_2025_COLUMN_MAP = {
    "Arrestee Type": "TYPE",
    "Arrest Year": "YEAR",
    "Arrest Date": "DATE_",
    "Arrest Hour": "HOUR",
    "CCN": "CCN",
    "Arrest Number#": "ARREST_NUMBER",
    "Age": "AGE",
    "Defendant PSA": "DEFENDANT_PSA",
    "Defendant District": "DEFENDANT_DISTRICT",
    "Defendant Race": "RACE",
    "Defendant Ethnicity": "ETHNICITY",
    "Defendant Sex": "SEX",
    "Arrest Category": "CATEGORY",
    "Charge Description": "DESCRIPTION",
    "Arrest Location PSA": "ARREST_PSA",
    "Arrest Location District": "ARREST_DISTRICT",
    "Arrest Block GEOX": "ARREST_BLOCKX",
    "Arrest Block GEOY": "ARREST_BLOCKY",
    "Arrest Latitude": "ARREST_LATITUDE",
    "Arrest Longitude": "ARREST_LONGITUDE",
    "Offense Location PSA": "OFFENSE_PSA",
    "Offense Location District": "OFFENSE_DISTRICT",
    "Offense Block GEOX": "OFFENSE_BLOCKX",
    "Offense Block GEOY": "OFFENSE_BLOCKY",
    "Offense Latitude": "OFFENSE_LATITUDE",
    "Offense Longitude": "OFFENSE_LONGITUDE",
}


def load_raw(path: Path = RAW_ARRESTS, path_2025: Path = RAW_ARRESTS_2025) -> pd.DataFrame:
    base = pd.read_csv(path, low_memory=False, dtype=str)
    new = pd.read_csv(path_2025, low_memory=False, dtype=str).rename(columns=_2025_COLUMN_MAP)
    common_cols = [c for c in base.columns if c in new.columns]
    df = pd.concat([base[common_cols], new[common_cols]], ignore_index=True)
    return df.drop_duplicates(subset="CCN")


def spatial_join(df: pd.DataFrame, wards_path: Path = RAW_WARDS, smd_path: Path = RAW_SMD) -> pd.DataFrame:
    """Add ward, SMD, and ANC columns via point-in-polygon spatial join."""
    wards = gpd.read_file(wards_path)
    smd = gpd.read_file(smd_path)

    df["geometry"] = df.apply(
        lambda row: Point(row["arrest_longitude"], row["arrest_latitude"]), axis=1
    )
    gdf = gpd.GeoDataFrame(df.copy(), geometry="geometry", crs="EPSG:4326").reset_index(drop=True)

    gdf = gpd.sjoin(gdf, wards[["WARD", "NAME", "geometry"]], how="left", predicate="within").reset_index(drop=True)
    gdf = gdf.drop(columns=["index_right"])

    gdf = gpd.sjoin(
        gpd.GeoDataFrame(gdf, geometry="geometry", crs="EPSG:4326").reset_index(drop=True),
        smd[["SMD_ID", "ANC_ID", "geometry"]],
        how="left",
        predicate="within",
    ).reset_index(drop=True)
    gdf = gdf.drop(columns=["index_right", "geometry"])

    return pd.DataFrame(gdf)


def run(raw_path: Path = RAW_ARRESTS, raw_path_2025: Path = RAW_ARRESTS_2025, output_path: Path = CLEAN_ARRESTS) -> pd.DataFrame:
    """Load, clean, spatially enrich, and save arrest data.

    Returns the cleaned DataFrame (for testing without writing to disk).
    Pass output_path=None to skip writing.
    """
    df = load_raw(raw_path, raw_path_2025)
    df = data_cleanup(df, "DATE_")
    df = arrest_category_cleanup(df)
    df = spatial_join(df)

    df.columns = [c.lower() for c in df.columns]
    df = df.dropna(subset=["ward"])
    df["ward"] = df["ward"].astype(int)
    df["year"] = df["date"].dt.year

    print(f"Arrests by ward:\n{df['ward'].value_counts().sort_index()}")
    print(f"Missing ward: {df['ward'].isna().sum()}")
    print(f"Missing SMD: {df['smd_id'].isna().sum()}")
    print(f"Missing ANC: {df['anc_id'].isna().sum()}")
    print(f"Missing PSA: {df['arrest_psa'].isna().sum()}")
    print(f"Missing category: {df['category'].isna().sum()}")

    if output_path is not None:
        df.to_csv(output_path, index=False, compression="gzip")
        print(f"Wrote {len(df):,} rows to {output_path}")

    return df


if __name__ == "__main__":
    run()

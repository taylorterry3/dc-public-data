"""ETL pipeline for DC adult arrest data."""

import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from pathlib import Path

from scripts.etl.common import data_cleanup, arrest_category_cleanup

RAW_ARRESTS = Path("data/raw/Adult_Arrests.csv.gz")
RAW_WARDS = Path("data/raw/Wards_from_2022.geojson")
RAW_SMD = Path("data/raw/Single_Member_District_from_2023.geojson")
CLEAN_ARRESTS = Path("data/clean/arrest_data.csv.gz")


def load_raw(path: Path = RAW_ARRESTS) -> pd.DataFrame:
    return pd.read_csv(path, low_memory=False, dtype=str)


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


def run(raw_path: Path = RAW_ARRESTS, output_path: Path = CLEAN_ARRESTS) -> pd.DataFrame:
    """Load, clean, spatially enrich, and save arrest data.

    Returns the cleaned DataFrame (for testing without writing to disk).
    Pass output_path=None to skip writing.
    """
    df = load_raw(raw_path)
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

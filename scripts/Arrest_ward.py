#!/usr/bin/env python

import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import numpy as np

# Read the arrest data
arrest_data = pd.read_csv("../data/clean/arrest_data.csv.gz", low_memory=False)

# Read the ward shapefile
wards = gpd.read_file("../data/raw/Wards_from_2022.geojson")

# Create geometry column for arrest points
arrest_data["geometry"] = arrest_data.apply(
    lambda row: Point(row["arrest_longitude"], row["arrest_latitude"]), axis=1
)

# Convert arrest data to GeoDataFrame
arrest_gdf = gpd.GeoDataFrame(
    arrest_data, geometry="geometry", crs="EPSG:4326"  # WGS84 coordinate system
)

# Perform spatial join
arrests_with_wards = gpd.sjoin(
    arrest_gdf, wards[["WARD", "NAME", "geometry"]], how="left", predicate="within"
)

# Drop the geometry column and save
arrests_with_wards = arrests_with_wards.drop(columns=["geometry"])
arrests_with_wards.to_csv(
    "../data/clean/arrest_data_with_wards.csv.gz", index=False, compression="gzip"
)

# Print some stats to verify the join
print("\nArrests by ward:")
print(arrests_with_wards["WARD"].value_counts().sort_index())

print("\nArrests with no ward (should be 0):")
print(arrests_with_wards["WARD"].isna().sum())

#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import numpy as np
from tqdm import tqdm

# Set style for plots
plt.style.use("seaborn-v0_8")  # Using a built-in style
sns.set_palette("husl")

print("Reading data...")
# Read the data
arrest_data = pd.read_csv(
    "../data/clean/arrest_data.csv.gz",
    low_memory=False,
)

# Parse date columns and ensure consistent timezone handling
arrest_data["date"] = pd.to_datetime(arrest_data["date_"], format="mixed", utc=True)
arrest_data = arrest_data.dropna(subset=["date"])  # Remove rows with invalid dates

print("\nColumns in the data:")
print(arrest_data.columns.tolist())
print("\nSample of date values:")
print(arrest_data["date"].head())

print("\nDate range in data:")
print(f"Earliest date: {arrest_data.date.min()}")
print(f"Latest date: {arrest_data.date.max()}")

print("\nYears in data:")
print(sorted(arrest_data.date.dt.year.unique()))

# Convert ward numbers to integers, handling NaN values
arrest_data["WARD"] = arrest_data["WARD"].fillna(-1).astype(int)
arrest_data = arrest_data[
    arrest_data.WARD > 0
]  # Remove any rows with invalid ward numbers

# Create reports directory if it doesn't exist
reports_dir = Path("../reports/wards")
reports_dir.mkdir(parents=True, exist_ok=True)


def generate_ward_report(ward_num):
    """Generate a markdown report for a specific ward."""
    # Filter data for this ward
    ward_data = arrest_data[arrest_data.WARD == ward_num].copy()

    # Calculate basic statistics
    total_arrests = len(ward_data)
    arrests_per_year = ward_data.groupby(ward_data.date.dt.year).size()
    recent_arrests = len(ward_data[ward_data.date.dt.year >= 2023])

    # Calculate 2024 arrests
    arrests_2024 = len(ward_data[ward_data.date.dt.year == 2024])

    # Calculate 2023 arrests
    arrests_2023 = len(ward_data[ward_data.date.dt.year == 2023])

    # Calculate 2021-2023 average
    arrests_2021_2023 = (
        len(
            ward_data[
                (ward_data.date.dt.year >= 2021) & (ward_data.date.dt.year <= 2023)
            ]
        )
        / 3
    )

    # Calculate first and second half of 2024
    arrests_2024_h1 = len(
        ward_data[(ward_data.date.dt.year == 2024) & (ward_data.date.dt.month <= 6)]
    )
    arrests_2024_h2 = len(
        ward_data[(ward_data.date.dt.year == 2024) & (ward_data.date.dt.month > 6)]
    )

    # Calculate percentage changes
    pct_change_2023 = (
        ((arrests_2024 - arrests_2023) / arrests_2023 * 100) if arrests_2023 > 0 else 0
    )
    pct_change_avg = (
        ((arrests_2024 - arrests_2021_2023) / arrests_2021_2023 * 100)
        if arrests_2021_2023 > 0
        else 0
    )

    # Calculate top categories for 2024
    ward_data_2024 = ward_data[ward_data.date.dt.year == 2024]
    ward_data_2023 = ward_data[ward_data.date.dt.year == 2023]
    ward_data_2024_h1 = ward_data[
        (ward_data.date.dt.year == 2024) & (ward_data.date.dt.month <= 6)
    ]
    ward_data_2024_h2 = ward_data[
        (ward_data.date.dt.year == 2024) & (ward_data.date.dt.month > 6)
    ]

    # Calculate monthly trends
    ward_data["month_year"] = ward_data.date.dt.strftime("%Y-%m")
    monthly_trends = ward_data.groupby("month_year").size()
    monthly_trends.index = pd.to_datetime(monthly_trends.index + "-01")

    # Calculate absolute changes for all categories
    all_categories = pd.concat(
        [
            ward_data_2024.category.value_counts(),
            ward_data_2023.category.value_counts(),
        ],
        axis=1,
    ).fillna(0)
    all_categories.columns = ["2024", "2023"]
    all_categories["change"] = all_categories["2024"] - all_categories["2023"]
    all_categories["pct_change"] = (
        (all_categories["2024"] - all_categories["2023"]) / all_categories["2023"] * 100
    ).fillna(0)
    # Filter out categories with 0 in either period
    all_categories = all_categories[
        (all_categories["2024"] > 0) & (all_categories["2023"] > 0)
    ]
    top_changes = all_categories.nlargest(5, "pct_change")

    # Calculate changes between first and second half of 2024
    half_comparison = pd.concat(
        [
            ward_data_2024_h2.category.value_counts(),
            ward_data_2024_h1.category.value_counts(),
        ],
        axis=1,
    ).fillna(0)
    half_comparison.columns = ["H2", "H1"]
    half_comparison["pct_change"] = (
        (half_comparison["H2"] - half_comparison["H1"]) / half_comparison["H1"] * 100
    ).fillna(0)
    # Filter out categories with 0 in either period
    half_comparison = half_comparison[
        (half_comparison["H2"] > 0) & (half_comparison["H1"] > 0)
    ]
    top_half_changes = half_comparison.nlargest(5, "pct_change")

    # Create plots with optimized settings
    plt.figure(figsize=(12, 6))
    monthly_trends.plot(kind="line", title=f"Ward {ward_num} Monthly Arrests")
    plt.xlabel("Date")
    plt.ylabel("Number of Arrests")

    # Get unique years from the data
    years = sorted(ward_data.date.dt.year.unique())

    # Create tick marks for January of each year
    year_ticks = [pd.Timestamp(f"{year}-01-01") for year in years]
    plt.xticks(year_ticks, years, rotation=0)

    # Add grid lines for better readability
    plt.grid(True, axis="x", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.savefig(reports_dir / f"ward_{ward_num}_monthly_trends.png", dpi=100)
    plt.close()

    # Calculate category distribution
    plt.figure(figsize=(10, 6))
    ward_data.category.value_counts().head(10).plot(kind="bar")
    plt.xticks(rotation=45, ha="right")
    plt.title(f"Ward {ward_num} Top 10 Arrest Categories")
    plt.xlabel("Category")
    plt.ylabel("Number of Arrests")
    plt.tight_layout()
    plt.savefig(reports_dir / f"ward_{ward_num}_categories.png", dpi=100)
    plt.close()

    # Generate descriptive text
    description = f"""# Ward {ward_num} Arrest Analysis Report

## Overview
In 2024 there were {arrests_2024:,} adult arrests in Ward {ward_num}, a {pct_change_2023:+.1f}% change from 2023 and a {pct_change_avg:+.1f}% change from the 2021-2023 average. The second half of 2024 saw {arrests_2024_h2:,} arrests, compared to {arrests_2024_h1:,} in the first half.

## Top Arrest Categories in 2024
| Category | 2024 | 2023 | Change |
|----------|------|------|---------|
"""
    for category in ward_data_2024.category.value_counts().head(5).index:
        count_2024 = len(ward_data_2024[ward_data_2024.category == category])
        count_2023 = len(ward_data_2023[ward_data_2023.category == category])
        pct_change = (
            ((count_2024 - count_2023) / count_2023 * 100) if count_2023 > 0 else 0
        )
        description += (
            f"| {category} | {count_2024:,} | {count_2023:,} | {pct_change:+.1f}% |\n"
        )

    description += f"""
## Categories with Largest Percentage Increases from 2023
| Category | 2024 | 2023 | Change |
|----------|------|------|---------|
"""
    for category in top_changes.index:
        count_2024 = int(top_changes.loc[category, "2024"])
        count_2023 = int(top_changes.loc[category, "2023"])
        pct_change = top_changes.loc[category, "pct_change"]
        description += (
            f"| {category} | {count_2024:,} | {count_2023:,} | {pct_change:+.1f}% |\n"
        )

    description += f"""
## Categories with Largest Percentage Increases (H2 vs H1 2024)
| Category | H2 2024 | H1 2024 | Change |
|----------|---------|---------|---------|
"""
    for category in top_half_changes.index:
        count_h2 = int(top_half_changes.loc[category, "H2"])
        count_h1 = int(top_half_changes.loc[category, "H1"])
        pct_change = top_half_changes.loc[category, "pct_change"]
        description += (
            f"| {category} | {count_h2:,} | {count_h1:,} | {pct_change:+.1f}% |\n"
        )

    description += f"""
## Monthly Trends
![Monthly Arrest Trends](ward_{ward_num}_monthly_trends.png)

## Category Distribution
![Top 10 Arrest Categories](ward_{ward_num}_categories.png)
"""

    # Save the report
    with open(reports_dir / f"ward_{ward_num}_report.md", "w") as f:
        f.write(description)


def main():
    # Get all wards
    wards = sorted(arrest_data.WARD.unique())

    print(f"Generating reports for {len(wards)} wards...")

    # Generate reports for all wards with progress bar
    for ward in tqdm(wards, desc="Generating ward reports"):
        generate_ward_report(ward)

    print("Ward reports have been generated in the reports/wards directory.")


if __name__ == "__main__":
    main()

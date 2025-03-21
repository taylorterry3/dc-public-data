#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import numpy as np
from tqdm import tqdm

# Set style for plots
plt.style.use("seaborn-v0_8")  # Using a built-in style
sns.set_palette("Set2")  # Changed from "husl" to "Set2" for better contrast

print("Reading data...")
# Read the data
arrest_data = pd.read_csv(
    "data/clean/arrest_data.csv.gz",
    low_memory=False,
)

# Parse the date column
arrest_data["date"] = pd.to_datetime(arrest_data["date"])

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
reports_dir = Path("reports/wards")
reports_dir.mkdir(parents=True, exist_ok=True)


def format_percentage(value):
    """Format a percentage value with a + sign for positive values."""
    try:
        value_int = int(round(float(value)))
        if value_int > 0:
            return "+" + str(value_int) + "%"
        return str(value_int) + "%"
    except (ValueError, TypeError):
        return "0%"


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
    monthly_trends.plot(kind="line")
    plt.title(f"Ward {ward_num} Monthly Arrests", fontsize=16, pad=20)
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
    plt.figure(figsize=(12, 8))

    # Get all categories and sort alphabetically
    all_categories = sorted(
        set(ward_data_2023.category.unique()) | set(ward_data_2024.category.unique())
    )

    # Create data for grouped bars
    categories_2023 = ward_data_2023.category.value_counts()
    categories_2024 = ward_data_2024.category.value_counts()

    # Ensure all categories are present in both series
    categories_2023 = categories_2023.reindex(all_categories).fillna(0)
    categories_2024 = categories_2024.reindex(all_categories).fillna(0)

    # Create grouped bar plot
    y_pos = np.arange(len(all_categories))
    width = 0.35

    plt.barh(y_pos - width / 2, categories_2023, width, label="2023")
    plt.barh(y_pos + width / 2, categories_2024, width, label="2024")

    plt.yticks(y_pos, all_categories)
    plt.xlabel("Number of Arrests")
    plt.title(f"Ward {ward_num} Arrest Categories", fontsize=16, pad=20)
    plt.legend()
    plt.gca().invert_yaxis()  # Invert y-axis to show ascending alphabetical order
    plt.tight_layout()
    plt.savefig(reports_dir / f"ward_{ward_num}_categories.png", dpi=100)
    plt.close()

    # Generate descriptive text
    description = "## Ward {} MPD Adult Arrest Summary, 2023-2024\n\n".format(ward_num)
    description += "### Overview\n"
    description += "In 2024 there were {:,} adult arrests in Ward {}, a {} change from 2023 and a {} change from the 2021-2023 average. The second half of 2024 saw {:,} arrests, compared to {:,} in the first half.\n\n".format(
        arrests_2024,
        ward_num,
        format_percentage(pct_change_2023),
        format_percentage(pct_change_avg),
        arrests_2024_h2,
        arrests_2024_h1,
    )

    description += "### Top Arrest Categories in 2024\n"
    description += "| Category | 2023 | 2024 | Change |\n"
    description += "|----------|------:|------:|---------:|\n"

    for category in ward_data_2024.category.value_counts().head(5).index:
        count_2024 = len(ward_data_2024[ward_data_2024.category == category])
        count_2023 = len(ward_data_2023[ward_data_2023.category == category])
        pct_change = (
            ((count_2024 - count_2023) / count_2023 * 100) if count_2023 > 0 else 0
        )
        description += "| {} | {:,} | {:,} | {} |\n".format(
            category, count_2023, count_2024, format_percentage(pct_change)
        )

    description += "\n### Arrest Categories with Largest Increase 2023-2024\n"
    description += "| Category | 2023 | 2024 | Change |\n"
    description += "|----------|------:|------:|---------:|\n"

    for category in top_changes.index:
        count_2024 = int(top_changes.loc[category, "2024"])
        count_2023 = int(top_changes.loc[category, "2023"])
        pct_change = top_changes.loc[category, "pct_change"]
        description += "| {} | {:,} | {:,} | {} |\n".format(
            category, count_2023, count_2024, format_percentage(pct_change)
        )

    description += "\n### Arrest Categories with Largest Increase H1-H2 2024\n"
    description += "| Category | H1 2024 | H2 2024 | Change |\n"
    description += "|----------|---------:|---------:|---------:|\n"

    for category in top_half_changes.index:
        count_h2 = int(top_half_changes.loc[category, "H2"])
        count_h1 = int(top_half_changes.loc[category, "H1"])
        pct_change = top_half_changes.loc[category, "pct_change"]
        description += "| {} | {:,} | {:,} | {} |\n".format(
            category, count_h1, count_h2, format_percentage(pct_change)
        )

    description += "\n### Monthly Trends\n"
    description += "![Monthly Arrest Trends](ward_{}_monthly_trends.png)\n\n".format(
        ward_num
    )
    description += "### Arrests by Category, 2023-2024\n"
    description += "![Arrests by category](ward_{}_categories.png)\n".format(ward_num)

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

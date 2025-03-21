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
reports_dir = Path("reports")
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


def generate_ward_report(df, ward_num):
    """Generate a report for a specific ward."""
    # Filter data for the ward
    ward_df = df[df["WARD"] == ward_num]

    # Calculate ward statistics
    arrests_2024 = len(ward_df[ward_df["year"] == 2024])
    arrests_2023 = len(ward_df[ward_df["year"] == 2023])
    arrests_2021_2023 = len(ward_df[ward_df["year"].isin([2021, 2022, 2023])])
    arrests_2024_h1 = len(ward_df[(ward_df["year"] == 2024) & (ward_df["month"] <= 6)])
    arrests_2024_h2 = len(ward_df[(ward_df["year"] == 2024) & (ward_df["month"] > 6)])

    # Calculate percentage changes
    pct_change_2023 = (
        ((arrests_2024 - arrests_2023) / arrests_2023 * 100) if arrests_2023 > 0 else 0
    )
    pct_change_avg = (
        ((arrests_2024 - arrests_2021_2023 / 3) / (arrests_2021_2023 / 3) * 100)
        if arrests_2021_2023 > 0
        else 0
    )
    pct_change_h1_h2 = (
        ((arrests_2024_h2 - arrests_2024_h1) / arrests_2024_h1 * 100)
        if arrests_2024_h1 > 0
        else 0
    )

    # Get top categories for 2024
    top_categories_2024 = (
        ward_df[ward_df["year"] == 2024]["category"].value_counts().head(10)
    )
    top_categories_2023 = ward_df[ward_df["year"] == 2023]["category"].value_counts()

    # Calculate category changes for all categories
    category_changes = []
    for category in ward_df["category"].unique():
        count_2024 = len(
            ward_df[(ward_df["year"] == 2024) & (ward_df["category"] == category)]
        )
        count_2023 = len(
            ward_df[(ward_df["year"] == 2023) & (ward_df["category"] == category)]
        )
        if (
            count_2023 > 0 or count_2024 > 0
        ):  # Only include if there were arrests in either year
            pct_change = (
                ((count_2024 - count_2023) / count_2023 * 100)
                if count_2023 > 0
                else float("inf")
            )
            category_changes.append((category, count_2023, count_2024, pct_change))

    # Sort by percentage change
    category_changes.sort(key=lambda x: x[3], reverse=True)

    # Get top 10 categories by frequency for the first table
    top_10_categories = top_categories_2024.index.tolist()
    top_10_changes = [
        change for change in category_changes if change[0] in top_10_categories
    ]
    # Sort by 2024 count for the top categories table
    top_10_changes.sort(key=lambda x: x[2], reverse=True)  # x[2] is the 2024 count

    # Get categories with largest H1-H2 changes
    categories_h1_h2 = []
    for category in ward_df["category"].unique():
        h1_count = len(
            ward_df[
                (ward_df["year"] == 2024)
                & (ward_df["month"] <= 6)
                & (ward_df["category"] == category)
            ]
        )
        h2_count = len(
            ward_df[
                (ward_df["year"] == 2024)
                & (ward_df["month"] > 6)
                & (ward_df["category"] == category)
            ]
        )
        if h1_count > 0:
            pct_change = (h2_count - h1_count) / h1_count * 100
            categories_h1_h2.append((category, h1_count, h2_count, pct_change))

    # Sort by percentage change
    categories_h1_h2.sort(key=lambda x: x[3], reverse=True)

    # Calculate citywide statistics for comparison
    citywide_2024 = len(df[df["year"] == 2024])
    citywide_2023 = len(df[df["year"] == 2023])
    citywide_2021_2023 = len(df[df["year"].isin([2021, 2022, 2023])])
    citywide_2024_h1 = len(df[(df["year"] == 2024) & (df["month"] <= 6)])
    citywide_2024_h2 = len(df[(df["year"] == 2024) & (df["month"] > 6)])

    citywide_pct_change_2023 = (
        ((citywide_2024 - citywide_2023) / citywide_2023 * 100)
        if citywide_2023 > 0
        else 0
    )
    citywide_pct_change_avg = (
        ((citywide_2024 - citywide_2021_2023 / 3) / (citywide_2021_2023 / 3) * 100)
        if citywide_2021_2023 > 0
        else 0
    )
    citywide_pct_change_h1_h2 = (
        ((citywide_2024_h2 - citywide_2024_h1) / citywide_2024_h1 * 100)
        if citywide_2024_h1 > 0
        else 0
    )

    # Generate descriptive text
    description = "## Ward {} MPD Adult Arrest Summary, 2023-2024\n\n".format(ward_num)
    description += "### Overview\n"
    description += "In 2024 there were {:,} adult arrests in Ward {}, a {} change from 2023 (citywide: {}) and a {} change from the 2021-2023 average (citywide: {}). The second half of 2024 saw {:,} arrests, compared to {:,} in the first half.\n\n".format(
        arrests_2024,
        ward_num,
        format_percentage(pct_change_2023),
        format_percentage(citywide_pct_change_2023),
        format_percentage(pct_change_avg),
        format_percentage(citywide_pct_change_avg),
        arrests_2024_h2,
        arrests_2024_h1,
    )

    description += "### Top Arrest Categories in 2024\n"
    description += "The table below shows the most common types of arrests in Ward {} during 2024, compared with 2023 counts. For each category, the ward-specific and citywide percentage changes are shown to provide context.\n\n".format(
        ward_num
    )
    description += (
        "| Category | 2023 | 2024 | Ward {} Change | Citywide Change |\n".format(
            ward_num
        )
    )
    description += "|----------|------:|------:|---------:|----------------:|\n"
    for category, count_2023, count_2024, pct_change in top_10_changes:
        citywide_count_2024 = len(
            df[(df["year"] == 2024) & (df["category"] == category)]
        )
        citywide_count_2023 = len(
            df[(df["year"] == 2023) & (df["category"] == category)]
        )
        citywide_pct_change = (
            ((citywide_count_2024 - citywide_count_2023) / citywide_count_2023 * 100)
            if citywide_count_2023 > 0
            else 0
        )
        description += "| {} | {:,} | {:,} | {} | {} |\n".format(
            category,
            count_2023,
            count_2024,
            format_percentage(pct_change),
            format_percentage(citywide_pct_change),
        )

    description += "\n### Arrest Categories with Largest Increase 2023-2024\n"
    description += "This table highlights the arrest categories that saw the largest percentage increases in Ward {} from 2023 to 2024. The citywide changes are shown for comparison to help identify whether these trends are ward-specific or part of broader patterns.\n\n".format(
        ward_num
    )
    description += (
        "| Category | 2023 | 2024 | Ward {} Change | Citywide Change |\n".format(
            ward_num
        )
    )
    description += "|----------|------:|------:|---------:|----------------:|\n"
    # Filter out categories with infinite change (new in 2024) and get top 10
    finite_changes = [c for c in category_changes if c[3] != float("inf")]
    for category, count_2023, count_2024, pct_change in finite_changes[:10]:
        citywide_count_2024 = len(
            df[(df["year"] == 2024) & (df["category"] == category)]
        )
        citywide_count_2023 = len(
            df[(df["year"] == 2023) & (df["category"] == category)]
        )
        citywide_pct_change = (
            ((citywide_count_2024 - citywide_count_2023) / citywide_count_2023 * 100)
            if citywide_count_2023 > 0
            else 0
        )
        description += "| {} | {:,} | {:,} | {} | {} |\n".format(
            category,
            count_2023,
            count_2024,
            format_percentage(pct_change),
            format_percentage(citywide_pct_change),
        )

    description += "\n### Arrest Categories with Largest Increase H1-H2 2024\n"
    description += "The following table compares arrest counts between the first half (H1) and second half (H2) of 2024 in Ward {}. This comparison helps identify emerging trends within the year. Categories are sorted by the magnitude of change between halves.\n\n".format(
        ward_num
    )
    description += (
        "| Category | H1 2024 | H2 2024 | Ward {} Change | Citywide Change |\n".format(
            ward_num
        )
    )
    description += "|----------|---------:|---------:|---------:|----------------:|\n"
    for category, h1_count, h2_count, pct_change in categories_h1_h2[:10]:
        citywide_h1 = len(
            df[(df["year"] == 2024) & (df["month"] <= 6) & (df["category"] == category)]
        )
        citywide_h2 = len(
            df[(df["year"] == 2024) & (df["month"] > 6) & (df["category"] == category)]
        )
        citywide_pct_change = (
            ((citywide_h2 - citywide_h1) / citywide_h1 * 100) if citywide_h1 > 0 else 0
        )
        description += "| {} | {:,} | {:,} | {} | {} |\n".format(
            category,
            h1_count,
            h2_count,
            format_percentage(pct_change),
            format_percentage(citywide_pct_change),
        )

    description += "\n### Monthly Trends\n"
    description += "The line graph below shows the month-by-month pattern of total arrests in Ward {} over time. This visualization helps identify seasonal patterns and longer-term trends in arrest volumes. Note that all arrest locations are based on current ward boundaries.\n\n".format(
        ward_num
    )
    description += "![Monthly Arrest Trends](ward_{}_monthly_trends.png)\n\n".format(
        ward_num
    )
    description += "### Arrests by Category, 2023-2024\n"
    description += "This chart compares the distribution of arrests across different categories between 2023 and 2024 in Ward {}. The side-by-side bars allow for easy comparison of how the composition of arrests has changed year over year.\n\n".format(
        ward_num
    )
    description += "![Arrests by category](ward_{}_categories.png)\n".format(ward_num)

    return description


def generate_citywide_report(df):
    """Generate a citywide report with data from all wards."""
    # Calculate citywide statistics
    arrests_2024 = len(df[df["year"] == 2024])
    arrests_2023 = len(df[df["year"] == 2023])
    arrests_2021_2023 = len(df[df["year"].isin([2021, 2022, 2023])])
    arrests_2024_h1 = len(df[(df["year"] == 2024) & (df["month"] <= 6)])
    arrests_2024_h2 = len(df[(df["year"] == 2024) & (df["month"] > 6)])

    # Calculate percentage changes
    pct_change_2023 = (
        ((arrests_2024 - arrests_2023) / arrests_2023 * 100) if arrests_2023 > 0 else 0
    )
    pct_change_avg = (
        ((arrests_2024 - arrests_2021_2023 / 3) / (arrests_2021_2023 / 3) * 100)
        if arrests_2021_2023 > 0
        else 0
    )
    pct_change_h1_h2 = (
        ((arrests_2024_h2 - arrests_2024_h1) / arrests_2024_h1 * 100)
        if arrests_2024_h1 > 0
        else 0
    )

    # Get top categories for 2024
    top_categories_2024 = df[df["year"] == 2024]["category"].value_counts().head(10)
    top_categories_2023 = df[df["year"] == 2023]["category"].value_counts()

    # Calculate category changes for all categories
    category_changes = []
    for category in df["category"].unique():
        count_2024 = len(df[(df["year"] == 2024) & (df["category"] == category)])
        count_2023 = len(df[(df["year"] == 2023) & (df["category"] == category)])
        if (
            count_2023 > 0 or count_2024 > 0
        ):  # Only include if there were arrests in either year
            pct_change = (
                ((count_2024 - count_2023) / count_2023 * 100)
                if count_2023 > 0
                else float("inf")
            )
            category_changes.append((category, count_2023, count_2024, pct_change))

    # Sort by percentage change
    category_changes.sort(key=lambda x: x[3], reverse=True)

    # Get top 10 categories by frequency for the first table
    top_10_categories = top_categories_2024.index.tolist()
    top_10_changes = [
        change for change in category_changes if change[0] in top_10_categories
    ]
    # Sort by 2024 count for the top categories table
    top_10_changes.sort(key=lambda x: x[2], reverse=True)  # x[2] is the 2024 count

    # Get categories with largest H1-H2 changes
    categories_h1_h2 = []
    for category in df["category"].unique():
        h1_count = len(
            df[(df["year"] == 2024) & (df["month"] <= 6) & (df["category"] == category)]
        )
        h2_count = len(
            df[(df["year"] == 2024) & (df["month"] > 6) & (df["category"] == category)]
        )
        if h1_count > 0:
            pct_change = (h2_count - h1_count) / h1_count * 100
            categories_h1_h2.append((category, h1_count, h2_count, pct_change))

    # Sort by percentage change
    categories_h1_h2.sort(key=lambda x: x[3], reverse=True)

    # Generate descriptive text
    description = "## DC MPD Adult Arrest Summary, 2023-2024\n\n"
    description += "### Overview\n"
    description += "In 2024 there were {:,} adult arrests citywide, a {} change from 2023 and a {} change from the 2021-2023 average. The second half of 2024 saw {:,} arrests, compared to {:,} in the first half.\n\n".format(
        arrests_2024,
        format_percentage(pct_change_2023),
        format_percentage(pct_change_avg),
        arrests_2024_h2,
        arrests_2024_h1,
    )

    description += "### Top Arrest Categories in 2024\n"
    description += "| Category | 2023 | 2024 | Change |\n"
    description += "|----------|------:|------:|---------:|\n"
    for category, count_2023, count_2024, pct_change in top_10_changes:
        description += "| {} | {:,} | {:,} | {} |\n".format(
            category, count_2023, count_2024, format_percentage(pct_change)
        )

    description += "\n### Arrest Categories with Largest Increase 2023-2024\n"
    description += "| Category | 2023 | 2024 | Change |\n"
    description += "|----------|------:|------:|---------:|\n"
    # Filter out categories with infinite change (new in 2024) and get top 10
    finite_changes = [c for c in category_changes if c[3] != float("inf")]
    for category, count_2023, count_2024, pct_change in finite_changes[:10]:
        description += "| {} | {:,} | {:,} | {} |\n".format(
            category, count_2023, count_2024, format_percentage(pct_change)
        )

    description += "\n### Arrest Categories with Largest Increase H1-H2 2024\n"
    description += "| Category | H1 2024 | H2 2024 | Change |\n"
    description += "|----------|---------:|---------:|---------:|\n"
    for category, h1_count, h2_count, pct_change in categories_h1_h2[:10]:
        description += "| {} | {:,} | {:,} | {} |\n".format(
            category, h1_count, h2_count, format_percentage(pct_change)
        )

    description += "\n### Monthly Trends\n"
    description += "![Monthly Arrest Trends](citywide_monthly_trends.png)\n\n"
    description += "### Arrests by Category, 2023-2024\n"
    description += "![Arrests by category](citywide_categories.png)\n"

    return description


def generate_citywide_plots(df, reports_dir):
    """Generate plots for citywide data."""
    # Monthly trends plot
    plt.figure(figsize=(12, 6))
    monthly_trends = df.groupby("month_year").size()
    monthly_trends.index = pd.to_datetime(monthly_trends.index + "-01")
    monthly_trends.plot(kind="line")
    plt.title("DC Monthly Arrests", fontsize=16, pad=20)
    plt.xlabel("Date")
    plt.ylabel("Number of Arrests")

    # Get unique years from the data
    years = sorted(df["date"].dt.year.unique())

    # Create tick marks for January of each year
    year_ticks = [pd.Timestamp(f"{year}-01-01") for year in years]
    plt.xticks(year_ticks, years, rotation=0)

    # Add grid lines for better readability
    plt.grid(True, axis="x", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.savefig(reports_dir / "citywide_monthly_trends.png", dpi=100)
    plt.close()

    # Category distribution plot
    plt.figure(figsize=(12, 8))

    # Get data for 2023 and 2024
    df_2023 = df[df["year"] == 2023]
    df_2024 = df[df["year"] == 2024]

    # Get all categories and sort alphabetically
    all_categories = sorted(
        set(df_2023["category"].unique()) | set(df_2024["category"].unique())
    )

    # Create data for grouped bars
    categories_2023 = df_2023["category"].value_counts()
    categories_2024 = df_2024["category"].value_counts()

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
    plt.title("DC Arrest Categories", fontsize=16, pad=20)
    plt.legend()
    plt.gca().invert_yaxis()  # Invert y-axis to show ascending alphabetical order
    plt.tight_layout()
    plt.savefig(reports_dir / "citywide_categories.png", dpi=100)
    plt.close()


def generate_ward_plots(df, ward_num, reports_dir):
    """Generate plots for a specific ward."""
    # Filter data for the ward
    ward_df = df[df["WARD"] == ward_num]

    # Monthly trends plot
    plt.figure(figsize=(12, 6))
    monthly_trends = ward_df.groupby("month_year").size()
    monthly_trends.index = pd.to_datetime(monthly_trends.index + "-01")
    monthly_trends.plot(kind="line")
    plt.title(f"Ward {ward_num} Monthly Arrests", fontsize=16, pad=20)
    plt.xlabel("Date")
    plt.ylabel("Number of Arrests")

    # Get unique years from the data
    years = sorted(ward_df["date"].dt.year.unique())

    # Create tick marks for January of each year
    year_ticks = [pd.Timestamp(f"{year}-01-01") for year in years]
    plt.xticks(year_ticks, years, rotation=0)

    # Add grid lines for better readability
    plt.grid(True, axis="x", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.savefig(reports_dir / f"ward_{ward_num}_monthly_trends.png", dpi=100)
    plt.close()

    # Category distribution plot
    plt.figure(figsize=(12, 8))

    # Get data for 2023 and 2024
    ward_df_2023 = ward_df[ward_df["year"] == 2023]
    ward_df_2024 = ward_df[ward_df["year"] == 2024]

    # Get all categories and sort alphabetically
    all_categories = sorted(
        set(ward_df_2023["category"].unique()) | set(ward_df_2024["category"].unique())
    )

    # Create data for grouped bars
    categories_2023 = ward_df_2023["category"].value_counts()
    categories_2024 = ward_df_2024["category"].value_counts()

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


def main():
    # Read the data
    print("Reading data...")
    df = pd.read_csv("data/clean/arrest_data.csv.gz")
    df["date"] = pd.to_datetime(df["date"])
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["month_year"] = df["date"].dt.strftime("%Y-%m")

    # Create reports directory if it doesn't exist
    reports_dir = Path("reports")
    reports_dir.mkdir(parents=True, exist_ok=True)

    # Generate citywide plots and report
    print("Generating citywide report...")
    generate_citywide_plots(df, reports_dir)
    citywide_report = generate_citywide_report(df)
    with open(reports_dir / "citywide_report.md", "w") as f:
        f.write(citywide_report)

    # Generate ward reports
    print("Generating reports for {} wards...".format(len(df["WARD"].unique())))
    for ward_num in tqdm(df["WARD"].unique(), desc="Generating ward reports"):
        # Generate plots for the ward
        generate_ward_plots(df, ward_num, reports_dir)
        # Generate the report
        ward_report = generate_ward_report(df, ward_num)
        with open(reports_dir / f"ward_{ward_num}_report.md", "w") as f:
            f.write(ward_report)

    print("\nWard reports have been generated in the reports directory.")


if __name__ == "__main__":
    main()

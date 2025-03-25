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
        if value == float("inf"):
            return "N/A"
        if value == float("-inf"):
            return "N/A"
        value_int = int(round(float(value)))
        if value_int > 0:
            return "+" + str(value_int) + "%"
        return str(value_int) + "%"
    except (ValueError, TypeError):
        return "0%"


def format_table_row(category, count1, count2, pct_change, citywide_pct_change=None):
    """Format a table row with consistent styling."""
    if citywide_pct_change is not None:
        return "| {} | {:,} | {:,} | {} | {} |\n".format(
            category,
            count1,
            count2,
            format_percentage(pct_change),
            format_percentage(citywide_pct_change),
        )
    return "| {} | {:,} | {:,} | {} |\n".format(
        category, count1, count2, format_percentage(pct_change)
    )


def generate_category_table(df, changes, ward_num=None, is_citywide=False):
    """Generate a markdown table from category changes.

    Args:
        df: The full dataset for calculating citywide stats
        changes: List of (category, count1, count2, pct_change) tuples
        ward_num: Ward number for ward-specific tables
        is_citywide: Whether this is the citywide report
    """
    table = ""
    if ward_num:
        table += (
            "| Category | 2023 | 2024 | Ward {} Change | Citywide Change |\n".format(
                ward_num
            )
        )
        table += "|----------|------:|------:|---------:|----------------:|\n"
    else:
        table += "| Category | 2023 | 2024 | Change |\n"
        table += "|----------|------:|------:|---------:|\n"

    if not changes:
        # If no changes, add a row indicating no data
        if ward_num:
            table += "| No arrest data available for 2024 | - | - | - | - |\n"
        else:
            table += "| No arrest data available for 2024 | - | - | - |\n"
        return table

    for category, count_2023, count_2024, pct_change in changes:
        if not is_citywide:
            citywide_count_2024 = len(
                df[(df["year"] == 2024) & (df["category"] == category)]
            )
            citywide_count_2023 = len(
                df[(df["year"] == 2023) & (df["category"] == category)]
            )
            citywide_pct_change = (
                (
                    (citywide_count_2024 - citywide_count_2023)
                    / citywide_count_2023
                    * 100
                )
                if citywide_count_2023 > 0
                else 0
            )
            table += format_table_row(
                category, count_2023, count_2024, pct_change, citywide_pct_change
            )
        else:
            table += format_table_row(category, count_2023, count_2024, pct_change)

    return table


def generate_h1h2_table(df, changes, ward_num=None, is_citywide=False):
    """Generate a markdown table for H1-H2 comparisons."""
    table = ""
    if ward_num:
        table += "| Category | H1 2024 | H2 2024 | Ward {} Change | Citywide Change |\n".format(
            ward_num
        )
        table += "|----------|---------:|---------:|---------:|----------------:|\n"
    else:
        table += "| Category | H1 2024 | H2 2024 | Change |\n"
        table += "|----------|---------:|---------:|---------:|\n"

    if not changes:
        # If no changes, add a row indicating no data
        if ward_num:
            table += "| No arrest data available for 2024 | - | - | - | - |\n"
        else:
            table += "| No arrest data available for 2024 | - | - | - |\n"
        return table

    for category, h1_count, h2_count, pct_change in changes:
        if not is_citywide:
            citywide_h1 = len(
                df[
                    (df["year"] == 2024)
                    & (df["month"] <= 6)
                    & (df["category"] == category)
                ]
            )
            citywide_h2 = len(
                df[
                    (df["year"] == 2024)
                    & (df["month"] > 6)
                    & (df["category"] == category)
                ]
            )
            citywide_pct_change = (
                ((citywide_h2 - citywide_h1) / citywide_h1 * 100)
                if citywide_h1 > 0
                else 0
            )
            table += format_table_row(
                category, h1_count, h2_count, pct_change, citywide_pct_change
            )
        else:
            table += format_table_row(category, h1_count, h2_count, pct_change)

    return table


def calculate_category_changes(df, year_filter):
    """Calculate changes in arrest categories between years or periods."""
    category_changes = []
    for category in df["category"].unique():
        count_2024 = len(df[(year_filter) & (df["category"] == category)])
        count_2023 = len(df[(df["year"] == 2023) & (df["category"] == category)])
        # Handle division by zero cases
        if count_2023 == 0:
            if count_2024 == 0:
                pct_change = 0  # No change if both years are 0
            else:
                pct_change = float(
                    "inf"
                )  # Infinite increase if going from 0 to non-zero
        else:
            pct_change = (count_2024 - count_2023) / count_2023 * 100
        category_changes.append((category, count_2023, count_2024, pct_change))
    return category_changes


def calculate_h1h2_changes(df):
    """Calculate changes between H1 and H2 of 2024."""
    categories_h1_h2 = []
    for category in df["category"].unique():
        h1_count = len(
            df[(df["year"] == 2024) & (df["month"] <= 6) & (df["category"] == category)]
        )
        h2_count = len(
            df[(df["year"] == 2024) & (df["month"] > 6) & (df["category"] == category)]
        )
        # Handle division by zero cases
        if h1_count == 0:
            if h2_count == 0:
                pct_change = 0  # No change if both halves are 0
            else:
                pct_change = float(
                    "inf"
                )  # Infinite increase if going from 0 to non-zero
        else:
            pct_change = (h2_count - h1_count) / h1_count * 100
        categories_h1_h2.append((category, h1_count, h2_count, pct_change))
    return categories_h1_h2


def calculate_arrest_statistics(df):
    """Calculate basic arrest statistics for a dataset."""
    stats = {}

    # Basic counts
    stats["arrests_2024"] = len(df[df["year"] == 2024])
    stats["arrests_2023"] = len(df[df["year"] == 2023])
    stats["arrests_2021_2023"] = len(df[df["year"].isin([2021, 2022, 2023])])
    stats["arrests_2024_h1"] = len(df[(df["year"] == 2024) & (df["month"] <= 6)])
    stats["arrests_2024_h2"] = len(df[(df["year"] == 2024) & (df["month"] > 6)])

    # Percentage changes
    stats["pct_change_2023"] = (
        ((stats["arrests_2024"] - stats["arrests_2023"]) / stats["arrests_2023"] * 100)
        if stats["arrests_2023"] > 0
        else 0
    )
    stats["pct_change_avg"] = (
        (
            (stats["arrests_2024"] - stats["arrests_2021_2023"] / 3)
            / (stats["arrests_2021_2023"] / 3)
            * 100
        )
        if stats["arrests_2021_2023"] > 0
        else 0
    )

    # Category analysis
    stats["category_changes"] = calculate_category_changes(df, df["year"] == 2024)

    # Get top 10 categories from 2023 if no 2024 data
    if stats["arrests_2024"] == 0:
        stats["top_10_categories"] = (
            df[df["year"] == 2023]["category"].value_counts().head(10).index.tolist()
        )
    else:
        stats["top_10_categories"] = (
            df[df["year"] == 2024]["category"].value_counts().head(10).index.tolist()
        )

    stats["top_10_changes"] = [
        change
        for change in stats["category_changes"]
        if change[0] in stats["top_10_categories"]
    ]
    stats["top_10_changes"].sort(
        key=lambda x: x[2], reverse=True
    )  # x[2] is the 2024 count

    # H1-H2 changes
    stats["categories_h1_h2"] = calculate_h1h2_changes(df)
    stats["categories_h1_h2"].sort(
        key=lambda x: x[3], reverse=True
    )  # Sort by percentage change

    return stats


def calculate_arrests_per_officer(df, officers_df):
    """Calculate average arrests per officer for different time periods."""
    stats = {}

    # Calculate average arrests per officer for 2016-2019
    arrests_2016_2019 = df[df["year"].between(2016, 2019)].groupby("year").size()
    officers_2016_2019 = officers_df[officers_df["year"].between(2016, 2019)].set_index(
        "year"
    )["officers"]
    arrests_per_officer_2016_2019 = (arrests_2016_2019 / officers_2016_2019).mean()

    # Calculate average arrests per officer for 2021-2023
    arrests_2021_2023 = df[df["year"].between(2021, 2023)].groupby("year").size()
    officers_2021_2023 = officers_df[officers_df["year"].between(2021, 2023)].set_index(
        "year"
    )["officers"]
    arrests_per_officer_2021_2023 = (arrests_2021_2023 / officers_2021_2023).mean()

    return arrests_per_officer_2016_2019, arrests_per_officer_2021_2023


def generate_ward_report(df, ward_num, officers_df):
    """Generate a report for a specific ward."""
    # Filter data for the ward and calculate statistics
    ward_df = df[df["WARD"] == ward_num]
    ward_stats = calculate_arrest_statistics(ward_df)
    citywide_stats = calculate_arrest_statistics(df)

    # Calculate arrests per officer statistics
    arrests_per_officer_2016_2019, arrests_per_officer_2021_2023 = (
        calculate_arrests_per_officer(df, officers_df)
    )

    # Generate report text
    description = "# Ward {} MPD Adult Arrest Summary, 2023-2024\n\n".format(ward_num)

    # Add background section
    description += "## Background\n\n"
    description += "MPD recently made its annual public release of Adult Arrests data, covering {:,} arrests in 2024. ".format(
        citywide_stats["arrests_2024"]
    )
    description += "This data represents the first full year of data available since Chief Smith took office in November of 2023, "
    description += "and reveals major changes in policing strategy over that timeframe. This report begins with an overview of "
    description += (
        "citywide trends, and then explores the data specific to Ward {}.\n\n".format(
            ward_num
        )
    )

    description += "This adult arrest data is taken from the Open Data DC website. DC resident and data scientist Taylor Terry "
    description += "maintains an archive of this and other DC public data at https://github.com/taylorterry3/dc-public-data. "
    description += "A complete index of these reports for each Ward is available at "
    description += "http://bit.ly/4iG0Uht. "
    description += "Taylor can be reached at taylor.terry@gmail.com.\n\n"

    # Add citywide overview with arrests per officer stats
    description += "### Citywide Overview\n\n"
    description += "In 2024 there were {:,} adult arrests citywide, a {} change from 2023 and a {} change from the ".format(
        citywide_stats["arrests_2024"],
        format_percentage(citywide_stats["pct_change_2023"]),
        format_percentage(citywide_stats["pct_change_avg"]),
    )
    description += "2021-2023 average. This represents a substantial increase in arrests per sworn officer, which fell sharply "
    description += "after 2020 from an average of {:.1f} arrests per officer per year in 2016-2019 to {:.1f} in 2021-2023.\n\n".format(
        arrests_per_officer_2016_2019, arrests_per_officer_2021_2023
    )

    # Continue with existing ward overview
    description += "### Ward {} Overview\n".format(ward_num)
    description += "In 2024 there were {:,} adult arrests in Ward {}, a {} change from 2023 (citywide: {}) and a {} change ".format(
        ward_stats["arrests_2024"],
        ward_num,
        format_percentage(ward_stats["pct_change_2023"]),
        format_percentage(citywide_stats["pct_change_2023"]),
        format_percentage(ward_stats["pct_change_avg"]),
    )
    description += "from the 2021-2023 average (citywide: {}). The second half of 2024 saw {:,} arrests, compared to {:,} in the first half.\n\n".format(
        format_percentage(citywide_stats["pct_change_avg"]),
        ward_stats["arrests_2024_h2"],
        ward_stats["arrests_2024_h1"],
    )

    # Largest Increase section
    description += "\n### Arrest Categories with Largest Increase 2023-2024\n"
    description += "This table highlights the arrest categories that saw the largest percentage increases in Ward {} from 2023 to 2024. The citywide changes are shown for comparison to help identify whether these trends are ward-specific or part of broader patterns.\n\n".format(
        ward_num
    )
    finite_changes = [c for c in ward_stats["category_changes"] if c[3] != float("inf")]
    finite_changes.sort(key=lambda x: x[3], reverse=True)  # Sort by percentage change
    description += generate_category_table(df, finite_changes[:10], ward_num)

    # Top Categories section
    description += "### Top Arrest Categories in 2024\n"
    description += "The table below shows the most common types of arrests in Ward {} during 2024, compared with 2023 counts. For each category, the ward-specific and citywide percentage changes are shown to provide context.\n\n".format(
        ward_num
    )
    description += generate_category_table(df, ward_stats["top_10_changes"], ward_num)

    # H1-H2 Changes section
    description += "\n### Arrest Categories with Largest Increase H1-H2 2024\n"
    description += "The following table compares arrest counts between the first half (H1) and second half (H2) of 2024 in Ward {}. This comparison helps identify emerging trends within the year. Categories are sorted by the magnitude of change between halves.\n\n".format(
        ward_num
    )
    description += generate_h1h2_table(
        df, ward_stats["categories_h1_h2"][:10], ward_num
    )

    # Monthly Trends section - on its own page
    description += "\n\\newpage\n"
    description += "### Monthly Trends\n"
    description += "Figure 1 below shows the month-by-month pattern of total arrests in Ward {} over time. This visualization helps identify seasonal patterns and longer-term trends in arrest volumes. Note that all arrest locations are based on current ward boundaries.\n\n".format(
        ward_num
    )
    description += "![Monthly Arrest Trends](ward_{}_monthly_trends.png)\n\n".format(
        ward_num
    )

    # Category Distribution section - on its own page
    description += "\n\\newpage\n"
    description += "### Arrests by Category, 2023-2024\n"
    description += "Figure 2 below compares the distribution of arrests across different categories between 2023 and 2024 in Ward {}. The side-by-side bars allow for easy comparison of how the composition of arrests has changed year over year.\n\n".format(
        ward_num
    )
    description += "![Arrests by category](ward_{}_categories.png)\n".format(ward_num)

    return description


def generate_citywide_report(df, officers_df):
    """Generate a citywide report with data from all wards."""
    # Calculate statistics
    stats = calculate_arrest_statistics(df)

    # Calculate arrests per officer statistics
    arrests_per_officer_2016_2019, arrests_per_officer_2021_2023 = (
        calculate_arrests_per_officer(df, officers_df)
    )

    # Generate report text
    description = "# DC MPD Adult Arrest Summary, 2023-2024\n\n"
    description += "### Overview\n"
    description += "In 2024 there were {:,} adult arrests citywide, a {} change from 2023 and a {} change from the 2021-2023 average. The second half of 2024 saw {:,} arrests, compared to {:,} in the first half.\n\n".format(
        stats["arrests_2024"],
        format_percentage(stats["pct_change_2023"]),
        format_percentage(stats["pct_change_avg"]),
        stats["arrests_2024_h2"],
        stats["arrests_2024_h1"],
    )

    # Top Categories section
    description += "### Top Arrest Categories in 2024\n"
    description += "The table below shows the most common types of arrests citywide during 2024, compared with 2023 counts.\n\n"
    description += generate_category_table(
        df, stats["top_10_changes"], is_citywide=True
    )

    # Largest Increase section
    description += "\n### Arrest Categories with Largest Increase 2023-2024\n"
    description += "This table highlights the arrest categories that saw the largest percentage increases citywide from 2023 to 2024.\n\n"
    finite_changes = [c for c in stats["category_changes"] if c[3] != float("inf")]
    finite_changes.sort(key=lambda x: x[3], reverse=True)  # Sort by percentage change
    description += generate_category_table(df, finite_changes[:10], is_citywide=True)

    # H1-H2 Changes section
    description += "\n### Arrest Categories with Largest Increase H1-H2 2024\n"
    description += "The following table compares arrest counts between the first half (H1) and second half (H2) of 2024.\n\n"
    description += generate_h1h2_table(
        df, stats["categories_h1_h2"][:10], is_citywide=True
    )

    # Monthly Trends section - on its own page
    description += "\n\\newpage\n"
    description += "### Monthly Trends\n"
    description += "Figure 1 below shows the month-by-month pattern of total arrests citywide over time. This visualization helps identify seasonal patterns and longer-term trends in arrest volumes.\n\n"
    description += "![Monthly Arrest Trends](citywide_monthly_trends.png)\n\n"

    # Category Distribution section - on its own page
    description += "\n\\newpage\n"
    description += "### Arrests by Category, 2023-2024\n"
    description += "Figure 2 below compares the distribution of arrests across different categories between 2023 and 2024 citywide. The side-by-side bars allow for easy comparison of how the composition of arrests has changed year over year.\n\n"
    description += "![Arrests by category](citywide_categories.png)\n"

    return description


def create_monthly_trends_plot(df, title):
    """Create a line plot showing monthly arrest trends."""
    plt.figure(figsize=(12, 6))
    monthly_trends = df.groupby("month_year").size()
    monthly_trends.index = pd.to_datetime(monthly_trends.index + "-01")
    monthly_trends.plot(kind="line")
    plt.xlabel("Date", fontsize=16)
    plt.ylabel("Number of Arrests", fontsize=16)

    # Get unique years and create tick marks for January of each year
    years = sorted(df["date"].dt.year.unique())
    year_ticks = [pd.Timestamp(f"{year}-01-01") for year in years]
    plt.xticks(year_ticks, years, rotation=0, fontsize=14)
    plt.yticks(fontsize=14)

    # Add grid lines for better readability
    plt.grid(True, axis="x", linestyle="--", alpha=0.7)
    plt.tight_layout()


def create_category_distribution_plot(df_2023, df_2024, title):
    """Create a horizontal bar plot comparing arrest categories between years."""
    plt.figure(figsize=(12, 8))

    # Get all categories and sort alphabetically
    all_categories = sorted(
        set(df_2023["category"].unique()) | set(df_2024["category"].unique())
    )

    # Create data for grouped bars
    categories_2023 = (
        df_2023["category"].value_counts().reindex(all_categories).fillna(0)
    )
    categories_2024 = (
        df_2024["category"].value_counts().reindex(all_categories).fillna(0)
    )

    # Create grouped bar plot
    y_pos = np.arange(len(all_categories))
    width = 0.35

    plt.barh(y_pos - width / 2, categories_2023, width, label="2023")
    plt.barh(y_pos + width / 2, categories_2024, width, label="2024")

    plt.yticks(y_pos, all_categories, fontsize=14)
    plt.xticks(fontsize=14)
    plt.xlabel("Number of Arrests", fontsize=16)
    plt.legend(fontsize=20)
    plt.gca().invert_yaxis()  # Invert y-axis to show ascending alphabetical order
    plt.tight_layout()


def generate_citywide_plots(df, reports_dir):
    """Generate plots for citywide data."""
    create_monthly_trends_plot(df, "DC Monthly Arrests")
    plt.savefig(reports_dir / "citywide_monthly_trends.png", dpi=100)
    plt.close()

    create_category_distribution_plot(
        df[df["year"] == 2023], df[df["year"] == 2024], "DC Arrest Categories"
    )
    plt.savefig(reports_dir / "citywide_categories.png", dpi=100)
    plt.close()


def generate_ward_plots(df, ward_num, reports_dir):
    """Generate plots for a specific ward."""
    ward_df = df[df["WARD"] == ward_num]

    create_monthly_trends_plot(ward_df, f"Ward {ward_num} Monthly Arrests")
    plt.savefig(reports_dir / f"ward_{ward_num}_monthly_trends.png", dpi=100)
    plt.close()

    create_category_distribution_plot(
        ward_df[ward_df["year"] == 2023],
        ward_df[ward_df["year"] == 2024],
        f"Ward {ward_num} Arrest Categories",
    )
    plt.savefig(reports_dir / f"ward_{ward_num}_categories.png", dpi=100)
    plt.close()


def preprocess_data(df):
    """Preprocess the arrest data for analysis."""
    # Parse dates and extract components
    df["date"] = pd.to_datetime(df["date"])
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["month_year"] = df["date"].dt.strftime("%Y-%m")

    # Clean ward numbers
    df["WARD"] = df["WARD"].fillna(-1).astype(int)
    df = df[df.WARD > 0]  # Remove any rows with invalid ward numbers

    return df


def print_data_info(df):
    """Print information about the dataset."""
    print("\nColumns in the data:")
    print(df.columns.tolist())
    print("\nSample of date values:")
    print(df["date"].head())
    print("\nDate range in data:")
    print(f"Earliest date: {df.date.min()}")
    print(f"Latest date: {df.date.max()}")
    print("\nYears in data:")
    print(sorted(df.date.dt.year.unique()))


def main():
    """Main function to generate arrest reports."""
    # Set up directories
    reports_dir = Path("reports")
    reports_dir.mkdir(parents=True, exist_ok=True)

    # Read and preprocess data
    print("Reading data...")
    df = pd.read_csv("data/clean/arrest_data.csv.gz", low_memory=False)
    officers_df = pd.read_csv("data/clean/officers.csv")
    df = preprocess_data(df)
    print_data_info(df)

    # Generate citywide report and plots
    print("Generating citywide report...")
    generate_citywide_plots(df, reports_dir)
    citywide_report = generate_citywide_report(df, officers_df)
    with open(reports_dir / "citywide_report.md", "w") as f:
        f.write(citywide_report)

    # Generate ward reports and plots
    ward_count = len(df["WARD"].unique())
    print(f"Generating reports for {ward_count} wards...")
    for ward_num in tqdm(df["WARD"].unique(), desc="Generating ward reports"):
        generate_ward_plots(df, ward_num, reports_dir)
        ward_report = generate_ward_report(df, ward_num, officers_df)
        with open(reports_dir / f"ward_{ward_num}_report.md", "w") as f:
            f.write(ward_report)

    print("\nWard reports have been generated in the reports directory.")


if __name__ == "__main__":
    main()

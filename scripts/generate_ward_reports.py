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
    """Generate a markdown table from category changes."""
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

    # Get all categories and their changes
    all_categories = set(cat[0] for cat in changes)
    shown_categories = set(cat[0] for cat in changes[:10])  # First 10 categories
    other_categories = all_categories - shown_categories

    # Add the top 10 rows
    for category, count_2023, count_2024, pct_change in changes[:10]:
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

    # Calculate totals for other categories
    if other_categories:
        other_2023 = sum(
            count_2023 for cat, count_2023, _, _ in changes if cat in other_categories
        )
        other_2024 = sum(
            count_2024 for cat, _, count_2024, _ in changes if cat in other_categories
        )
        other_change = other_2024 - other_2023
        other_pct_change = (
            ((other_2024 - other_2023) / other_2023 * 100) if other_2023 > 0 else 0
        )

        if not is_citywide:
            citywide_other_2023 = len(
                df[(df["year"] == 2023) & df["category"].isin(other_categories)]
            )
            citywide_other_2024 = len(
                df[(df["year"] == 2024) & df["category"].isin(other_categories)]
            )
            citywide_other_pct_change = (
                (
                    (citywide_other_2024 - citywide_other_2023)
                    / citywide_other_2023
                    * 100
                )
                if citywide_other_2023 > 0
                else 0
            )
            table += format_table_row(
                "All Other Categories",
                other_2023,
                other_2024,
                other_pct_change,
                citywide_other_pct_change,
            )
        else:
            table += format_table_row(
                "All Other Categories", other_2023, other_2024, other_pct_change
            )

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

    # Get all categories and their changes
    all_categories = set(cat[0] for cat in changes)
    shown_categories = set(cat[0] for cat in changes[:10])  # First 10 categories
    other_categories = all_categories - shown_categories

    # Add the top 10 rows
    for category, h1_count, h2_count, pct_change in changes[:10]:
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

    # Calculate totals for other categories
    if other_categories:
        other_h1 = sum(
            h1_count for cat, h1_count, _, _ in changes if cat in other_categories
        )
        other_h2 = sum(
            h2_count for cat, _, h2_count, _ in changes if cat in other_categories
        )
        other_change = ((other_h2 - other_h1) / other_h1 * 100) if other_h1 > 0 else 0

        if not is_citywide:
            citywide_other_h1 = len(
                df[
                    (df["year"] == 2024)
                    & (df["month"] <= 6)
                    & df["category"].isin(other_categories)
                ]
            )
            citywide_other_h2 = len(
                df[
                    (df["year"] == 2024)
                    & (df["month"] > 6)
                    & df["category"].isin(other_categories)
                ]
            )
            citywide_other_change = (
                ((citywide_other_h2 - citywide_other_h1) / citywide_other_h1 * 100)
                if citywide_other_h1 > 0
                else 0
            )
            table += format_table_row(
                "All Other Categories",
                other_h1,
                other_h2,
                other_change,
                citywide_other_change,
            )
        else:
            table += format_table_row(
                "All Other Categories", other_h1, other_h2, other_change
            )

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


def calculate_category_changes_detail(df):
    """Calculate detailed changes in arrests by category between 2023 and 2024."""
    changes = {}
    for category in df["category"].unique():
        count_2024 = len(df[(df["year"] == 2024) & (df["category"] == category)])
        count_2023 = len(df[(df["year"] == 2023) & (df["category"] == category)])
        changes[category] = {
            "2024": count_2024,
            "2023": count_2023,
            "change": count_2024 - count_2023,
            "pct_change": (
                ((count_2024 - count_2023) / count_2023 * 100)
                if count_2023 > 0
                else float("inf")
            ),
        }
    return changes


def calculate_ward_level_changes(df):
    """Calculate changes in arrests by ward between 2023 and 2024."""
    ward_changes = []
    for ward in sorted(df["WARD"].unique()):
        ward_df = df[df["WARD"] == ward]
        count_2024 = len(ward_df[ward_df["year"] == 2024])
        count_2023 = len(ward_df[ward_df["year"] == 2023])
        change = count_2024 - count_2023
        pct_change = (
            ((count_2024 - count_2023) / count_2023 * 100)
            if count_2023 > 0
            else float("inf")
        )
        ward_changes.append(
            {
                "ward": ward,
                "2023": count_2023,
                "2024": count_2024,
                "change": change,
                "pct_change": pct_change,
            }
        )
    # Return sorted by ward number instead of change magnitude
    return sorted(ward_changes, key=lambda x: x["ward"])


def calculate_arrest_statistics(df):
    """Calculate basic arrest statistics for a dataset."""
    stats = {}

    # Basic counts
    stats["arrests_2024"] = len(df[df["year"] == 2024])
    stats["arrests_2023"] = len(df[df["year"] == 2023])
    stats["arrests_2021_2023"] = len(df[df["year"].isin([2021, 2022, 2023])])
    # Convert average to integer using round
    stats["avg_arrests_2021_2023"] = round(stats["arrests_2021_2023"] / 3)
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
            (stats["arrests_2024"] - stats["avg_arrests_2021_2023"])
            / stats["avg_arrests_2021_2023"]
            * 100
        )
        if stats["avg_arrests_2021_2023"] > 0
        else 0
    )

    # Category analysis
    stats["category_changes"] = calculate_category_changes(df, df["year"] == 2024)
    stats["category_changes_detail"] = calculate_category_changes_detail(df)
    stats["ward_changes"] = calculate_ward_level_changes(df)

    # Get top 10 categories
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

    # Calculate arrests per officer for 2024
    arrests_2024 = len(df[df["year"] == 2024])
    officers_2024 = officers_df[officers_df["year"] == 2024]["officers"].iloc[0]
    arrests_per_officer_2024 = arrests_2024 / officers_2024

    return (
        arrests_per_officer_2016_2019,
        arrests_per_officer_2021_2023,
        arrests_per_officer_2024,
    )


def generate_background_section(citywide_stats, is_citywide=False, ward_num=None):
    """Generate the background section text."""
    description = "# "
    if is_citywide:
        description += (
            "Metropolitan Police Department Adult Arrest Trends, 2023-2024\n\n"
        )
    else:
        description += f"Ward {ward_num} MPD Adult Arrest Trends, 2023-2024\n\n"

    description += "## Background\n\n"
    description += f"MPD recently made its annual public release of adult arrest data, covering {citywide_stats['arrests_2024']:,} arrests in 2024. "
    description += "This data represents the first full year of data available since Chief Smith took office in November of 2023, "

    if is_citywide:
        description += "and reveals major changes in policing strategy over that timeframe. This report covers data for the entire city, "
        description += "and reports with the same data broken down for each Ward are available at http://bit.ly/4iG0Uht. \n\n"
    else:
        description += "and reveals major changes in policing strategy over that timeframe. This report begins with an overview of "
        description += f"citywide trends, and then explores the data specific to Ward {ward_num}.\n\n"

    description += "This adult arrest data is taken from the Open Data DC website. DC resident and data scientist Taylor Terry "
    description += "maintains an archive of this and other DC public data at https://github.com/taylorterry3/dc-public-data. "
    if not is_citywide:
        description += (
            "A complete index of these reports for each Ward is available at "
        )
        description += "http://bit.ly/4iG0Uht. "
    description += "Taylor can be reached at taylor.terry@gmail.com.\n\n"

    return description


def create_officer_trends_plot(df, officers_df, stops_df):
    """Create a line plot showing arrests and stops per officer trends."""
    plt.figure(figsize=(12, 6))

    # Create monthly arrests data
    monthly_arrests = df.groupby(["year", "month"]).size().reset_index(name="arrests")
    monthly_arrests["date"] = pd.to_datetime(
        monthly_arrests[["year", "month"]].assign(day=1)
    )

    # Create monthly officers data
    officers_monthly = officers_df.copy()
    officers_monthly["date"] = pd.to_datetime(
        officers_monthly["year"].astype(str) + "-01-01"
    )

    # Merge arrests with officers and calculate rate
    merged_data = pd.merge_asof(
        monthly_arrests.sort_values("date"),
        officers_monthly[["date", "officers"]].sort_values("date"),
        on="date",
        direction="backward",
    )
    merged_data["arrests_per_officer"] = (
        merged_data["arrests"] / merged_data["officers"]
    )

    # Add stops data if available
    if stops_df is not None and not stops_df.empty:
        monthly_stops = (
            stops_df.groupby(["year", "month"]).size().reset_index(name="stops")
        )
        monthly_stops["date"] = pd.to_datetime(
            monthly_stops[["year", "month"]].assign(day=1)
        )

        # Skip the first month of stops data which appears to be incomplete
        # (likely only partial month of data collection)
        monthly_stops = monthly_stops.iloc[1:]

        # Merge stops with officers and calculate rate
        stops_merged = pd.merge_asof(
            monthly_stops.sort_values("date"),
            officers_monthly[["date", "officers"]].sort_values("date"),
            on="date",
            direction="backward",
        )
        stops_merged["stops_per_officer"] = (
            stops_merged["stops"] / stops_merged["officers"]
        )

        # Plot stops first (so it's behind arrests)
        plt.plot(
            stops_merged["date"],
            stops_merged["stops_per_officer"],
            color="blue",
            label="Stops per Officer per Month",
            alpha=0.8,
        )

    # Plot arrests
    plt.plot(
        merged_data["date"],
        merged_data["arrests_per_officer"],
        color="red",
        label="Arrests per Officer per Month",
        alpha=0.8,
    )

    plt.xlabel("Year", fontsize=16)
    plt.ylabel("Monthly Rate", fontsize=16)

    # Set x-axis ticks to show years
    years = sorted(df["year"].unique())
    year_ticks = [pd.Timestamp(f"{year}-01-01") for year in years]
    plt.xticks(year_ticks, years, rotation=0, fontsize=14)
    plt.yticks(fontsize=14)

    plt.grid(True, linestyle="--", alpha=0.7)
    plt.legend(fontsize=18)
    plt.tight_layout()


def generate_overview_section(
    df,
    ward_stats,
    arrests_per_officer_stats,
    officers_df,
    is_citywide=False,
    ward_num=None,
    citywide_stats=None,
):
    """Generate the overview section text."""
    description = "### "
    if is_citywide:
        description += "Citywide Changes in Arrest Patterns"
    else:
        description += "Citywide Changes in Arrest Patterns"
    description += "\n\n"

    # Always use citywide stats for this section
    stats_to_use = citywide_stats if not is_citywide else ward_stats

    # Keep the first sentence about total arrests and averages
    description += "In 2024 there were {:,} adult arrests citywide, a {} change from {:,} arrests in 2023 and a {} change from the 2021-2023 average of {:,}. ".format(
        stats_to_use["arrests_2024"],
        format_percentage(stats_to_use["pct_change_2023"]),
        stats_to_use["arrests_2023"],
        format_percentage(stats_to_use["pct_change_avg"]),
        stats_to_use["avg_arrests_2021_2023"],
    )

    # Get changes for Wards 1, 7, and 8
    ward_changes = stats_to_use["ward_changes"]
    ward_1_7_8_changes = [w for w in ward_changes if w["ward"] in [1, 7, 8]]
    other_ward_changes = [w for w in ward_changes if w["ward"] not in [1, 7, 8]]

    # Check if all three wards had large increases
    large_increase_wards = [w for w in ward_1_7_8_changes if w["change"] > 1000]

    if len(large_increase_wards) == 3:
        description += "The increase in arrests was concentrated in Wards 1, 7, and 8. "
        if other_ward_changes:
            # Sort other wards by change magnitude to find actual next biggest gain
            next_biggest = sorted(
                other_ward_changes, key=lambda x: abs(x["change"]), reverse=True
            )[0]
            description += "These wards each saw more than 1,000 additional arrests, while the next biggest gain was {:,} additional arrests in Ward {}.\n\n".format(
                next_biggest["change"], next_biggest["ward"]
            )
        else:
            description += "\n\n"
    else:
        description += "The changes in arrests varied significantly by ward.\n\n"

    # Add ward comparison table with all wards
    description += "| Ward | 2023 | 2024 | Change | Percent Change |\n"
    description += "|------|------:|------:|--------:|---------------:|\n"
    for ward_stat in sorted(ward_changes, key=lambda x: x["ward"]):
        description += "| {} | {:,} | {:,} | {:+,} | {} |\n".format(
            ward_stat["ward"],
            ward_stat["2023"],
            ward_stat["2024"],
            ward_stat["change"],
            format_percentage(ward_stat["pct_change"]),
        )
    description += "\n"

    # Move the category text before the table
    category_changes = stats_to_use["category_changes_detail"]
    category_text = []
    if "Traffic Violations" in category_changes:
        category_text.append(
            f"{category_changes['Traffic Violations']['change']:,} additional arrests for Traffic Violations"
        )
    if "Theft" in category_changes:
        category_text.append(f"{category_changes['Theft']['change']:,} for Theft")
    if "Narcotics" in category_changes:
        category_text.append(
            f"{category_changes['Narcotics']['change']:,} for Narcotics"
        )
    if "Liquor Law Violations" in category_changes:
        category_text.append(
            f"{category_changes['Liquor Law Violations']['change']:,} for Liquor Law Violations"
        )

    if category_text:
        description += (
            "Much of this increase in arrests was driven by "
            + ", ".join(category_text)
            + ". \n\n"
        )

    # Add top changes by volume table
    sorted_categories = sorted(
        category_changes.items(), key=lambda x: abs(x[1]["change"]), reverse=True
    )

    # Get top 4 and rest (changed from 5)
    top_4 = sorted_categories[:4]
    rest = sorted_categories[4:]  # Changed from 5
    rest_total_change = sum(cat[1]["change"] for cat in rest)
    rest_total_2023 = sum(cat[1]["2023"] for cat in rest)
    rest_pct_change = (
        (
            (sum(cat[1]["2024"] for cat in rest) - rest_total_2023)
            / rest_total_2023
            * 100
        )
        if rest_total_2023 > 0
        else 0
    )

    # Create the table
    description += "| Category | 2023 | 2024 | Change | Percent Change |\n"
    description += "|----------|------:|------:|--------:|---------------:|\n"

    # Add top 4 categories
    for category, stats in top_4:
        description += "| {} | {:,} | {:,} | {:+,} | {} |\n".format(
            category,
            stats["2023"],
            stats["2024"],
            stats["change"],
            format_percentage(stats["pct_change"]),
        )

    # Add the "All Other Categories" row
    description += "| All Other Categories | {:,} | {:,} | {:+,} | {} |\n".format(
        rest_total_2023,
        sum(cat[1]["2024"] for cat in rest),
        rest_total_change,
        format_percentage(rest_pct_change),
    )
    description += "\n"

    # Add page break and description before crosstab
    description += "\\newpage\n\n"
    description += "This crosstab shows the percentage change for these arrest categories by Ward from 2023 to 2024.\n\n"

    # Add ward by category crosstab
    # Get the top 4 categories from the previous table
    top_4_categories = [cat for cat, _ in top_4]

    # Create mapping for shorter category names
    category_short_names = {
        "Traffic Violations": "Traffic",
        "Liquor Law Violations": "Liquor",
        "All Other Categories": "Other",
    }

    # Create the crosstab header
    description += "|Category| W1 | W2 | W3 | W4 | W5 | W6 | W7 | W8 |\n"
    description += "|--------|---:|---:|---:|---:|---:|---:|---:|----:|\n"

    # For each category, calculate the percent change by ward
    for category in top_4_categories:
        # Use short name if available, otherwise use original name
        display_name = category_short_names.get(category, category)
        row = f"| {display_name}"
        for ward in range(1, 9):
            ward_df = df[df["WARD"] == ward]
            count_2023 = len(
                ward_df[(ward_df["year"] == 2023) & (ward_df["category"] == category)]
            )
            count_2024 = len(
                ward_df[(ward_df["year"] == 2024) & (ward_df["category"] == category)]
            )
            pct_change = (
                ((count_2024 - count_2023) / count_2023 * 100)
                if count_2023 > 0
                else float("inf")
            )
            row += f" | {format_percentage(pct_change)}"
        description += row + " |\n"

    # Add Other row (renamed from All Other Categories)
    description += "| Other"  # Using shorter name
    other_categories = set(category_changes.keys()) - set(top_4_categories)
    for ward in range(1, 9):
        ward_df = df[df["WARD"] == ward]
        count_2023 = len(
            ward_df[
                (ward_df["year"] == 2023) & ward_df["category"].isin(other_categories)
            ]
        )
        count_2024 = len(
            ward_df[
                (ward_df["year"] == 2024) & ward_df["category"].isin(other_categories)
            ]
        )
        pct_change = (
            ((count_2024 - count_2023) / count_2023 * 100)
            if count_2023 > 0
            else float("inf")
        )
        description += f" | {format_percentage(pct_change)}"
    description += " |\n\n"

    # Add Productivity per Officer section header
    description += "### Productivity per Officer\n\n"

    # Continue with the MPD officers text
    description += "MPD reported having {:,} sworn officers in 2024, meaning that {:,} arrests represents {:.1f} arrests per sworn officer for the year. ".format(
        officers_df[officers_df["year"] == 2024]["officers"].iloc[0],
        stats_to_use["arrests_2024"],
        arrests_per_officer_stats[2],  # 2024 value
    )
    description += "This is a substantial increase from the 2021-2023 average of {:.1f} arrests per officer per year, ".format(
        arrests_per_officer_stats[1]  # 2021-2023 average
    )
    description += "but is far from a return to the 2016-2019 average of {:.1f} arrests per officer. ".format(
        arrests_per_officer_stats[0]  # 2016-2019 average
    )
    description += "The chart below shows the trend in arrests per sworn officer over time, as well as the trend in stops per officer for periods when this data is available. (MPD stops data currently runs only through June of 2024, and the release schedule is irregular.)\n\n"

    # Always show the citywide officer trends plot
    description += "![Arrests and Stops per Officer](citywide_officer_trends.png)\n\n"

    # Add ward-specific overview section for ward reports
    if not is_citywide:
        description += "### Ward {} Overview\n\n".format(ward_num)
        description += "In 2024 there were {:,} adult arrests in Ward {}, a {} change from 2023 (citywide: {}) and a {} change ".format(
            ward_stats["arrests_2024"],
            ward_num,
            format_percentage(ward_stats["pct_change_2023"]),
            format_percentage(stats_to_use["pct_change_2023"]),
            format_percentage(ward_stats["pct_change_avg"]),
        )
        description += "from the 2021-2023 average (citywide: {}). ".format(
            format_percentage(stats_to_use["pct_change_avg"])
        )
        description += "The second half of 2024 saw {:,} arrests, compared to {:,} in the first half.\n\n".format(
            ward_stats["arrests_2024_h2"],
            ward_stats["arrests_2024_h1"],
        )

    return description


def generate_category_sections(df, stats, is_citywide=False, ward_num=None):
    """Generate the category analysis sections."""
    description = ""

    # Add page break before first category section
    description += "\n\\newpage\n"

    # Largest Increase section
    description += "### Arrest Categories with Largest Increase 2023-2024\n"
    if not is_citywide:
        description += f"This table highlights the arrest categories that saw the largest percentage increases in Ward {ward_num} from 2023 to 2024. The citywide changes are shown for comparison to help identify whether these trends are ward-specific or part of broader patterns.\n\n"
    else:
        description += "This table highlights the arrest categories that saw the largest percentage increases citywide from 2023 to 2024.\n\n"

    finite_changes = [c for c in stats["category_changes"] if c[3] != float("inf")]
    finite_changes.sort(key=lambda x: x[3], reverse=True)  # Sort by percentage change
    description += generate_category_table(
        df, finite_changes, ward_num if not is_citywide else None, is_citywide
    )

    # Top Categories section
    description += "### Top Arrest Categories in 2024\n"
    if not is_citywide:
        description += f"The table below shows the most common types of arrests in Ward {ward_num} during 2024, compared with 2023 counts. For each category, the ward-specific and citywide percentage changes are shown to provide context.\n\n"
    else:
        description += "The table below shows the most common types of arrests citywide during 2024, compared with 2023 counts.\n\n"

    # Sort by 2024 count (index 2) instead of percentage change
    top_categories = sorted(stats["category_changes"], key=lambda x: x[2], reverse=True)
    description += generate_category_table(
        df, top_categories, ward_num if not is_citywide else None, is_citywide
    )

    # H1-H2 Changes section
    description += "\n### Arrest Categories with Largest Increase H1-H2 2024\n"
    description += "Many areas of the city and types of crimes saw substantial changes in the pattern of arrests between the first half and second half of 2024. "
    if not is_citywide:
        description += f"The following table compares arrest counts between the first half (H1) and second half (H2) of 2024 in Ward {ward_num}. This comparison helps identify emerging trends within the year. Categories are sorted by the magnitude of change between halves.\n\n"
    else:
        description += "The following table compares arrest counts between the first half (H1) and second half (H2) of 2024.\n\n"
    description += generate_h1h2_table(
        df,
        stats["categories_h1_h2"],
        ward_num if not is_citywide else None,
        is_citywide,
    )

    return description


def generate_visualization_sections(is_citywide=False, ward_num=None):
    """Generate the visualization sections."""
    description = ""

    # Remove Monthly Trends section, keep only Category Distribution
    description += "\n\\newpage\n"
    description += "### Arrests by Category, 2023-2024\n"
    if not is_citywide:
        description += f"Figure 2 below compares the distribution of arrests across different categories between 2023 and 2024 in Ward {ward_num}. The side-by-side bars allow for easy comparison of how the composition of arrests has changed year over year.\n\n"
        description += f"![Arrests by category](ward_{ward_num}_categories.png)\n"
    else:
        description += "Figure 2 below compares the distribution of arrests across different categories between 2023 and 2024 citywide. The side-by-side bars allow for easy comparison of how the composition of arrests has changed year over year.\n\n"
        description += "![Arrests by category](citywide_categories.png)\n"

    return description


def generate_citywide_report(df, officers_df):
    """Generate a citywide report with data from all wards."""
    stats = calculate_arrest_statistics(df)
    arrests_per_officer_stats = calculate_arrests_per_officer(df, officers_df)

    description = generate_background_section(stats, is_citywide=True)
    description += generate_overview_section(
        df, stats, arrests_per_officer_stats, officers_df, is_citywide=True
    )
    description += generate_category_sections(df, stats, is_citywide=True)
    description += generate_visualization_sections(is_citywide=True)

    return description


def generate_ward_report(df, ward_num, officers_df):
    """Generate a report for a specific ward."""
    ward_df = df[df["WARD"] == ward_num]
    ward_stats = calculate_arrest_statistics(ward_df)
    citywide_stats = calculate_arrest_statistics(df)
    arrests_per_officer_stats = calculate_arrests_per_officer(df, officers_df)

    description = generate_background_section(citywide_stats, ward_num=ward_num)
    description += generate_overview_section(
        df,
        ward_stats,
        arrests_per_officer_stats,
        officers_df,
        ward_num=ward_num,
        citywide_stats=citywide_stats,
    )
    description += generate_category_sections(df, ward_stats, ward_num=ward_num)
    description += generate_visualization_sections(ward_num=ward_num)

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
    plt.figure(figsize=(12, 10))

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


def generate_citywide_plots(df, reports_dir, officers_df, stops_df=None):
    """Generate plots for citywide data."""
    # Remove monthly trends plot generation
    create_category_distribution_plot(
        df[df["year"] == 2023], df[df["year"] == 2024], "DC Arrest Categories"
    )
    plt.savefig(reports_dir / "citywide_categories.png", dpi=100)
    plt.close()

    create_officer_trends_plot(df, officers_df, stops_df)
    plt.savefig(reports_dir / "citywide_officer_trends.png", dpi=100)
    plt.close()


def generate_ward_plots(df, ward_num, reports_dir, officers_df, stops_df=None):
    """Generate plots for a specific ward."""
    ward_df = df[df["WARD"] == ward_num]

    # Remove monthly trends plot generation
    create_category_distribution_plot(
        ward_df[ward_df["year"] == 2023],
        ward_df[ward_df["year"] == 2024],
        f"Ward {ward_num} Arrest Categories",
    )
    plt.savefig(reports_dir / f"ward_{ward_num}_categories.png", dpi=100)
    plt.close()


def preprocess_data(df):
    """Preprocess the arrest or stops data for analysis."""
    # Parse dates and extract components
    df["date"] = pd.to_datetime(df["date"])
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["month_year"] = df["date"].dt.strftime("%Y-%m")

    # Clean ward numbers if present
    if "WARD" in df.columns:
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

    # Try to read stops data if available
    try:
        stops_df = pd.read_csv("data/clean/stop_data.csv.gz", low_memory=False)
        stops_df = preprocess_data(stops_df)  # Preprocess stops data
    except FileNotFoundError:
        stops_df = None

    df = preprocess_data(df)  # Preprocess arrest data
    print_data_info(df)

    # Generate citywide plots including officer trends
    print("Generating citywide report...")
    generate_citywide_plots(df, reports_dir, officers_df, stops_df)
    citywide_report = generate_citywide_report(df, officers_df)
    with open(reports_dir / "citywide_report.md", "w") as f:
        f.write(citywide_report)

    # Generate ward reports - officer trends plot already generated
    ward_count = len(df["WARD"].unique())
    print(f"Generating reports for {ward_count} wards...")
    for ward_num in tqdm(df["WARD"].unique(), desc="Generating ward reports"):
        generate_ward_plots(df, ward_num, reports_dir, officers_df, stops_df)
        ward_report = generate_ward_report(df, ward_num, officers_df)
        with open(reports_dir / f"ward_{ward_num}_report.md", "w") as f:
            f.write(ward_report)

    print("\nWard reports have been generated in the reports directory.")


if __name__ == "__main__":
    main()

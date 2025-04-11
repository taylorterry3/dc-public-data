#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import numpy as np
from tqdm import tqdm
from datetime import datetime

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
arrest_data["ward"] = arrest_data["ward"].fillna(-1).astype(int)
arrest_data = arrest_data[
    arrest_data.ward > 0
]  # Remove any rows with invalid ward numbers

# Create reports directory if it doesn't exist
reports_dir = Path("reports")
reports_dir.mkdir(parents=True, exist_ok=True)

REPORT_CONFIG = {
    "short_names": {
        "Traffic Violations": "Traffic",
        "Liquor Law Violations": "Liquor",
        "All Other Categories": "Other",
    },
    "plot_settings": {"figsize": (12, 6), "fontsize": 14, "grid_alpha": 0.7},
    "required_sections": [
        "Background",
        "Citywide Changes in Arrest Patterns",
        "Productivity per Officer",
        "Arrest Categories with Largest Increase 2023-2024",
        "Top Arrest Categories in 2024",
        "Arrests by Category, 2023-2024",
    ],
}


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


def generate_category_table(df, categories, year1=2023, year2=2024, is_h1h2=False):
    """Generate a markdown table showing category changes between two periods."""
    rows = []
    for category in categories:
        if is_h1h2:
            count1 = len(
                df[
                    (df["year"] == 2024)
                    & (df["month"] <= 6)
                    & (df["category"] == category)
                ]
            )
            count2 = len(
                df[
                    (df["year"] == 2024)
                    & (df["month"] > 6)
                    & (df["category"] == category)
                ]
            )
        else:
            count1 = len(df[(df["year"] == year1) & (df["category"] == category)])
            count2 = len(df[(df["year"] == year2) & (df["category"] == category)])

        change = count2 - count1
        pct_change = ((count2 - count1) / count1 * 100) if count1 > 0 else float("inf")

        rows.append(
            {
                "category": category,
                "count1": count1,
                "count2": count2,
                "change": change,
                "pct_change": pct_change,
            }
        )

    # Sort rows by percentage change, handling inf values
    rows.sort(
        key=lambda x: (
            -float("inf") if x["pct_change"] == float("inf") else x["pct_change"]
        ),
        reverse=True,
    )

    # Generate table header
    period1 = "H1 2024" if is_h1h2 else str(year1)
    period2 = "H2 2024" if is_h1h2 else str(year2)

    table = f"| Arrest Category | {period1} | {period2} | Change | % Change |\n"
    table += "|----------------|------:|------:|--------:|----------:|\n"

    # Add rows
    for row in rows:
        table += "| {} | {:,} | {:,} | {:+,} | {} |\n".format(
            row["category"],
            row["count1"],
            row["count2"],
            row["change"],
            format_percentage(row["pct_change"]),
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
    all_categories = set(cat["category"] for cat in changes)
    shown_categories = set(
        cat["category"] for cat in changes[:10]
    )  # First 10 categories
    other_categories = all_categories - shown_categories

    # Add the top 10 rows
    for category_data in changes[:10]:
        category = category_data["category"]
        h1_count = category_data["count1"]
        h2_count = category_data["count2"]
        pct_change = category_data["pct_change"]

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
            cat["count1"] for cat in changes if cat["category"] in other_categories
        )
        other_h2 = sum(
            cat["count2"] for cat in changes if cat["category"] in other_categories
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


def calculate_category_metrics(df, categories, year1, year2, is_h1h2=False):
    """Calculate metrics for categories between two periods.

    Args:
        df: DataFrame with arrest data
        categories: List of categories to analyze
        year1: First year/period
        year2: Second year/period
        is_h1h2: Boolean indicating if comparing H1 to H2
    """
    metrics = []
    for category in categories:
        if is_h1h2:
            count1 = len(
                df[
                    (df["year"] == 2024)
                    & (df["month"] <= 6)
                    & (df["category"] == category)
                ]
            )
            count2 = len(
                df[
                    (df["year"] == 2024)
                    & (df["month"] > 6)
                    & (df["category"] == category)
                ]
            )
        else:
            count1 = len(df[(df["year"] == year1) & (df["category"] == category)])
            count2 = len(df[(df["year"] == year2) & (df["category"] == category)])

        pct_change = ((count2 - count1) / count1 * 100) if count1 > 0 else float("inf")
        metrics.append(
            {
                "category": category,
                "count1": count1,
                "count2": count2,
                "change": count2 - count1,
                "pct_change": pct_change,
            }
        )
    return metrics


def calculate_arrest_statistics(df: pd.DataFrame) -> dict:
    """Calculate basic arrest statistics for a dataset."""
    stats = {}

    # Basic counts
    stats["arrests_2024"] = len(df[df["year"] == 2024])
    print(f"\nCalculating arrests_2024: {stats['arrests_2024']}")  # Debug output

    stats["arrests_2023"] = len(df[df["year"] == 2023])
    stats["arrests_2021_2023"] = len(df[df["year"].isin([2021, 2022, 2023])])
    # Convert average to integer using round
    stats["avg_arrests_2021_2023"] = (
        round(stats["arrests_2021_2023"] / 3) if stats["arrests_2021_2023"] > 0 else 0
    )
    stats["arrests_2024_h1"] = len(df[(df["year"] == 2024) & (df["month"] <= 6)])
    stats["arrests_2024_h2"] = len(df[(df["year"] == 2024) & (df["month"] > 6)])

    # Percentage changes - handle cases where we might not have data
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
    stats["category_changes"] = calculate_category_metrics(
        df, df["category"].unique(), 2023, 2024
    )

    # Convert category_changes_detail to dictionary format
    category_changes_detail = {}
    for metric in stats["category_changes"]:
        category_changes_detail[metric["category"]] = {
            "2023": metric["count1"],
            "2024": metric["count2"],
            "change": metric["change"],
            "pct_change": metric["pct_change"],
        }
    stats["category_changes_detail"] = category_changes_detail

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
        if change["category"] in stats["top_10_categories"]
    ]
    stats["top_10_changes"].sort(
        key=lambda x: x["count2"], reverse=True
    )  # Sort by 2024 count

    # H1-H2 changes
    stats["categories_h1_h2"] = calculate_category_metrics(
        df, df["category"].unique(), 2024, 2024, True
    )
    stats["categories_h1_h2"].sort(
        key=lambda x: x["pct_change"], reverse=True
    )  # Sort by percentage change

    return stats


def calculate_arrests_per_officer(df, officers_df):
    """Calculate average arrests per officer for different time periods."""
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

    # Debug output
    print("\nArrests per officer calculation debug:")
    print(f"arrests_2024: {arrests_2024}")
    print(f"officers_2024: {officers_2024}")
    print(f"arrests_per_officer_2024: {arrests_per_officer_2024}")

    return (
        arrests_per_officer_2016_2019,
        arrests_per_officer_2021_2023,
        arrests_per_officer_2024,
    )


def generate_background_section(citywide_stats: dict) -> str:
    """Generate the background section text."""
    description = (
        "# DC Metropolitan Police Department Adult Arrest Trends, 2023-2024\n\n"
    )
    description += "## Background\n\n"
    description += f"MPD recently made its annual public release of adult arrest data, covering {citywide_stats['arrests_2024']:,} arrests in 2024. "
    description += "This data represents the first full year of data available since Chief Smith took office in November of 2023, "
    description += "and reveals major changes in policing strategy over that timeframe. This report begins with some aggregate data and analysis, "
    description += f"and also includes appendices with tables and charts for each Ward, Police District, ANC, and PSA. \n\n"

    description += "This adult arrest data is taken from the Open Data DC website. DC resident and data scientist Taylor Terry "
    description += "maintains an archive of this and other DC public data at https://github.com/taylorterry3/dc-public-data. "
    description += (
        "The code used to generate this report is also available in that repository. "
    )
    description += f"This version of the report was generated on {datetime.now().strftime('%B %d, %Y')}. "
    description += "This report, including any updated versions, is available in Google Drive at bit.ly/4iG0Uht.\n\n"

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
    df: pd.DataFrame,
    citywide_stats: dict,
    arrests_per_officer_stats: tuple,
    officers_df: pd.DataFrame,
) -> str:
    """Generate the overview section text."""
    description = "### Citywide Changes in Arrest Patterns\n\n"

    # Keep the first sentence about total arrests and averages
    description += "In 2024 MPD made {:,} adult arrests citywide, a {} change from {:,} arrests in 2023 and a {} change from the 2021-2023 average of {:,}. ".format(
        citywide_stats["arrests_2024"],
        format_percentage(citywide_stats["pct_change_2023"]),
        citywide_stats["arrests_2023"],
        format_percentage(citywide_stats["pct_change_avg"]),
        citywide_stats["avg_arrests_2021_2023"],
    )

    # Get changes for Wards 1, 7, and 8
    ward_changes = citywide_stats.get("ward_changes", [])
    ward_1_7_8_changes = [w for w in ward_changes if w["ward"] in [1, 7, 8]]
    other_ward_changes = [w for w in ward_changes if w["ward"] not in [1, 7, 8]]

    # Directly state that Wards 1, 7, and 8 had large increases
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
    category_changes = citywide_stats.get("category_changes_detail", {})
    category_text = []
    if "Traffic Violations" in category_changes:
        category_text.append(
            f"{category_changes['Traffic Violations']['change']:,} additional arrests for Traffic Violations"
        )
    if "Theft" in category_changes:
        category_text.append(f"{category_changes['Theft']['change']:,} more for Theft")
    if "Narcotics" in category_changes:
        category_text.append(
            f"{category_changes['Narcotics']['change']:,} more for Narcotics"
        )
    if "Liquor Law Violations" in category_changes:
        category_text.append(
            f"{category_changes['Liquor Law Violations']['change']:,} more for Liquor Law Violations"
        )

    if category_text:
        description += (
            "Much of this increase in arrests was driven by "
            + ", ".join(category_text[:-1])  # Join all items except the last
            + ", and "  # Add ", and " before the last item
            + category_text[-1]  # Add the last item
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
    description += "| Arrest Category | 2023 | 2024 | Change | % Change |\n"
    description += "|----------------|------:|------:|--------:|----------:|\n"

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
    description += "This crosstab shows the percentage change for these arrest categories by Ward from 2023 to 2024. "
    description += "Note especially the roughly tenfold increase in Liquor Law Violation arrests in Wards 7 and 8, "
    description += (
        "as well as a similarly large increase in Traffic Violation arrests in Ward 7. "
    )
    description += (
        "Ward 1 saw fivefold increases in Liquor Law Violation and Narcotics arrests, "
    )
    description += "while Ward 5 saw a similar rate of increase in Liquor Law Violation Arrests. \n\n"

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

    # Debug information
    print("\nWard-by-category counts for 2023:")
    for ward in range(1, 9):
        ward_df = df[df["ward"] == ward]
        print(
            f"\nWard {ward} total 2023 arrests: {len(ward_df[ward_df['year'] == 2023])}"
        )
        for category in top_4_categories:
            count = len(
                ward_df[(ward_df["year"] == 2023) & (ward_df["category"] == category)]
            )
            print(f"  {category}: {count}")

    # For each category, calculate the percent change by ward
    for category in top_4_categories:
        # Use short name if available, otherwise use original name
        display_name = category_short_names.get(category, category)
        row = f"| {display_name}"
        for ward in range(1, 9):
            ward_df = df[df["ward"] == ward]
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
        ward_df = df[df["ward"] == ward]
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
        citywide_stats["arrests_2024"],
        arrests_per_officer_stats[2],  # 2024 value
    )
    description += "This is a substantial increase from the 2021-2023 average of {:.1f} arrests per officer per year, ".format(
        arrests_per_officer_stats[1]  # 2021-2023 average
    )
    description += "but is far from a return to the 2016-2019 average of {:.1f} arrests per officer. \n\n".format(
        arrests_per_officer_stats[0]  # 2016-2019 average
    )
    description += "The chart below shows the trend in arrests per sworn officer per month over time, as well as the trend in stops per officer for periods when this data is available. "
    description += "MPD stops data currently runs only from 2019 through June of 2024. The release schedule is irregular and MPD has historically refused to release this data "
    description += "in response to FOIA requests, and so it is unclear when the rest of the 2024 data will be available. "
    description += "\n\n"

    # Change the image reference to not include a title
    description += "![](citywide_officer_trends.png)\n\n"

    return description


def generate_category_sections(df: pd.DataFrame, stats: dict) -> str:
    """Generate the category analysis sections."""
    description = ""

    # Add page break before category section
    description += "\n\\newpage\n"

    # Add citywide category table
    description += "### Arrests by Category\n\n"
    description += "The table below shows the number of arrests by category citywide for the years 2023 and 2024, "
    description += "sorted by percentage change. "
    description += "Of particular note is that DWI arrests remained flat despite a greater than threefold increase in "
    description += "arrests for Traffic Violations. \n\n"

    # Get all categories and filter out NaN values
    categories = sorted(cat for cat in df["category"].unique() if pd.notna(cat))

    # Generate table using the updated generate_category_table function
    description += generate_category_table(df, categories)

    # Add the chart description and image
    description += "\n\\newpage\n"
    description += "\nThis chart presents the same data as above in a visual format, sorted by arrest category.\n\n"
    description += "![](citywide_categories.png)\n"

    return description


def generate_visualization_sections() -> str:
    """Generate the visualization sections."""
    return ""


def generate_citywide_plots(df, reports_dir, officers_df, stops_df=None):
    """Generate plots for citywide data."""
    create_plots(
        df, reports_dir=reports_dir, officers_df=officers_df, stops_df=stops_df
    )


def generate_ward_plots(df, ward_num, reports_dir, officers_df, stops_df=None):
    """Generate plots for a specific ward."""
    create_plots(df, "ward", ward_num, reports_dir, officers_df)


def generate_district_plots(df, district, reports_dir, officers_df, stops_df=None):
    """Generate plots for a specific district."""
    create_plots(df, "district", district, reports_dir, officers_df)


def generate_area_appendix(df, area_type, area_id):
    """Generate appendix section for a ward or district."""
    description = "\n\\newpage\n"
    # Capitalize area_type for display
    display_type = area_type.capitalize()
    if area_type.lower() == "district":
        description += f"## {area_id}\n\n"  # Just show district ID (e.g., "## 1D")
    else:
        description += f"## {display_type} {area_id}\n\n"  # Show "Ward X"

    # Get area-specific data
    area_col = "ward" if area_type.lower() == "ward" else "arrest_district"
    area_df = df[df[area_col] == area_id]

    # Calculate category-level changes
    categories = sorted(cat for cat in df["category"].unique() if pd.notna(cat))
    table = generate_category_table(area_df, categories)
    description += table

    # Use underscore in image reference to match the saved filename
    file_prefix = "ward" if area_type.lower() == "ward" else "district"
    description += f"\n![]({file_prefix}_{area_id}_categories.png)\n\n"

    return description


def generate_anc_appendix(df):
    """Generate appendix section for ANCs."""
    description = "\n\\newpage\n# Appendix 3: Data by ANC\n\n"
    ancs = sorted(df["anc_id"].unique())
    for anc in ancs:
        if anc:  # Skip empty strings
            # Add a new page before each ANC section
            description += f"\\newpage\n## ANC {anc}\n\n"
            # Get ANC-specific data
            anc_df = df[df["anc_id"] == anc]
            categories = sorted(cat for cat in df["category"].unique() if pd.notna(cat))
            table = generate_category_table(anc_df, categories)
            description += table
            # Sanitize the anc for the filename
            sanitized_anc = str(anc).replace(" ", "_").replace("/", "-")
            description += f"\n![](anc_{sanitized_anc}_categories.png)\n\n"
    return description


def generate_psa_appendix(df):
    """Generate appendix section for PSAs."""
    description = "\n\\newpage\n# Appendix 4: Data by PSA\n\n"
    psas = sorted(df["arrest_psa"].unique())
    for psa in psas:
        # Add a new page before each PSA section
        description += f"\\newpage\n## PSA {psa}\n\n"
        # Get PSA-specific data
        psa_df = df[df["arrest_psa"] == psa]
        categories = sorted(cat for cat in df["category"].unique() if pd.notna(cat))
        table = generate_category_table(psa_df, categories)
        description += table
        # Sanitize the psa for the filename
        sanitized_psa = str(psa).replace(" ", "_").replace("/", "-")
        description += f"\n![](psa_{sanitized_psa}_categories.png)\n\n"
    return description


def generate_report(df: pd.DataFrame, officers_df: pd.DataFrame) -> str:
    """Generate the complete report with citywide analysis and ward/district appendices."""
    print("\n=== Starting report generation ===")
    sections = []

    # Calculate citywide statistics
    print("Calculating citywide statistics...")
    citywide_stats = calculate_arrest_statistics(df)
    print(f"Citywide stats keys: {list(citywide_stats.keys())}")

    # Calculate arrests per officer using the same stats
    arrests_2024 = citywide_stats["arrests_2024"]
    officers_2024 = officers_df[officers_df["year"] == 2024]["officers"].iloc[0]
    arrests_per_officer_2024 = arrests_2024 / officers_2024

    # Calculate other periods
    arrests_2016_2019 = df[df["year"].between(2016, 2019)].groupby("year").size()
    officers_2016_2019 = officers_df[officers_df["year"].between(2016, 2019)].set_index(
        "year"
    )["officers"]
    arrests_per_officer_2016_2019 = (arrests_2016_2019 / officers_2016_2019).mean()

    arrests_2021_2023 = df[df["year"].between(2021, 2023)].groupby("year").size()
    officers_2021_2023 = officers_df[officers_df["year"].between(2021, 2023)].set_index(
        "year"
    )["officers"]
    arrests_per_officer_2021_2023 = (arrests_2021_2023 / officers_2021_2023).mean()

    arrests_per_officer_stats = (
        arrests_per_officer_2016_2019,
        arrests_per_officer_2021_2023,
        arrests_per_officer_2024,
    )

    print("Generating background section...")
    sections.append(generate_background_section(citywide_stats))

    print("Generating overview section...")
    sections.append(
        generate_overview_section(
            df,
            citywide_stats,
            arrests_per_officer_stats,
            officers_df,
        )
    )

    print("Generating category sections...")
    sections.append(generate_category_sections(df, citywide_stats))
    sections.append(generate_visualization_sections())

    # Add Ward Appendix
    print("Generating ward appendix...")
    sections.append("\n\\newpage\n# Appendix 1: Data by Ward\n\n")
    ward_numbers = sorted(df["ward"].unique())
    sections.append(
        generate_area_appendix(df, "ward", ward_numbers[0]).replace(
            "\n\\newpage\n", "\n"
        )
    )
    for ward_num in ward_numbers[1:]:
        sections.append(generate_area_appendix(df, "ward", ward_num))

    # Add District Appendix
    print("Generating district appendix...")
    sections.append("\n\\newpage\n# Appendix 2: Data by Police District\n\n")
    districts = sorted(
        dist for dist in df["arrest_district"].unique() if pd.notna(dist)
    )
    sections.append(
        generate_area_appendix(df, "district", districts[0]).replace(
            "\n\\newpage\n", "\n"
        )
    )
    for district in districts[1:]:
        sections.append(generate_area_appendix(df, "district", district))

    # Add ANC Appendix
    print("Generating ANC appendix...")
    sections.append(generate_anc_appendix(df))

    # Add PSA Appendix
    print("Generating PSA appendix...")
    sections.append(generate_psa_appendix(df))

    print("=== Report generation complete ===")
    return "\n".join(sections)


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

    # Ensure ANC and PSA are in all caps in the title
    title = title.replace("Anc", "ANC").replace("Psa", "PSA")
    plt.title(title, fontsize=20, fontweight="bold")

    plt.legend(fontsize=20)
    plt.gca().invert_yaxis()  # Invert y-axis to show ascending alphabetical order
    plt.tight_layout()


def create_plots(
    df, area_type=None, area_id=None, reports_dir=None, officers_df=None, stops_df=None
):
    """Generate plots for citywide, ward, district, ANC, or PSA data."""
    if area_type and area_id:
        # Determine the correct column based on area type
        if area_type == "ward":
            area_col = "ward"
        elif area_type == "district":
            area_col = "arrest_district"
        elif area_type == "anc":
            area_col = "anc_id"
        elif area_type == "psa":
            area_col = "arrest_psa"  # Fixed column name
        else:
            raise ValueError(f"Unsupported area type: {area_type}")

        # Filter data for specific area
        df = df[df[area_col] == area_id]
        # Use space instead of underscore in filename
        prefix = f"{area_type} {str(area_id)}"
    else:
        prefix = "citywide"

    # Sanitize the prefix to ensure it's a valid filename
    sanitized_prefix = prefix.replace(" ", "_").replace("/", "-")

    # Create category distribution plot
    create_category_distribution_plot(
        df[df["year"] == 2023],
        df[df["year"] == 2024],
        f"{prefix.title()} Arrests by Category",
    )
    # Use sanitized prefix in filename
    plt.savefig(reports_dir / f"{sanitized_prefix}_categories.png", dpi=100)
    plt.close()

    # Create officer trends plot for citywide only
    if not area_type:
        create_officer_trends_plot(df, officers_df, stops_df)
        plt.savefig(reports_dir / "citywide_officer_trends.png", dpi=100)
        plt.close()


def preprocess_data(df):
    """Preprocess the arrest or stops data for analysis."""
    # Parse dates and extract components
    print("\nDate parsing debug:")
    print(f"Number of rows before date parsing: {len(df)}")
    print(f"Number of 2024 arrests before date parsing: {len(df[df['year'] == 2024])}")
    print(f"Number of null dates: {df['date'].isnull().sum()}")

    # Convert date column to datetime
    df["date"] = pd.to_datetime(df["date"])

    # Use existing year column instead of creating a new one
    print(f"\nNumber of rows after date parsing: {len(df)}")
    print(f"Number of 2024 arrests after date parsing: {len(df[df['year'] == 2024])}")
    print(f"Number of invalid dates: {df['date'].isnull().sum()}")

    # Debug year column
    print("\nYear column debug:")
    print(f"Years in data: {sorted(df['year'].unique())}")
    print(f"2024 rows: {len(df[df['year'] == 2024])}")
    print(f"2023 rows: {len(df[df['year'] == 2023])}")

    # Extract month from date
    df["month"] = df["date"].dt.month
    df["month_year"] = df["date"].dt.strftime("%Y-%m")

    # Clean ward numbers if present
    if "ward" in df.columns:
        print("\nWard processing debug:")
        print(
            f"Number of 2024 arrests before ward processing: {len(df[df['year'] == 2024])}"
        )
        print("\nWard values before processing:")
        print(df["ward"].value_counts().sort_index())

        # Convert NaN and invalid ward numbers to "Unknown" instead of filtering them out
        df["ward"] = df["ward"].fillna("Unknown")
        df.loc[~df["ward"].astype(str).str.isdigit(), "ward"] = "Unknown"
        print("\nWard values after processing:")
        print(df["ward"].value_counts().sort_index())
        print(
            f"\nNumber of 2024 arrests after ward processing: {len(df[df['year'] == 2024])}"
        )

    # Standardize district column name if present
    district_col = next(
        (col for col in df.columns if col.lower() == "arrest_district"), None
    )
    if district_col and district_col != "arrest_district":
        df = df.rename(columns={district_col: "arrest_district"})

    # Ensure anc_id is treated as a string and handle NaNs
    if "anc_id" in df.columns:
        df["anc_id"] = df["anc_id"].fillna("Unknown").astype(str)

    # Ensure arrest_psa is treated as a string and handle NaNs
    if "arrest_psa" in df.columns:
        print("\nPSA processing debug:")
        print(
            f"Number of 2024 arrests before PSA processing: {len(df[df['year'] == 2024])}"
        )
        print("\nPSA values before processing:")
        print(df["arrest_psa"].value_counts())

        # Convert NaN to "Unknown"
        df["arrest_psa"] = df["arrest_psa"].fillna("Unknown")

        # Convert numeric values to strings without decimal points
        df["arrest_psa"] = df["arrest_psa"].apply(
            lambda x: (
                str(int(float(x)))
                if pd.notna(x) and str(x).replace(".", "").isdigit()
                else x
            )
        )

        # Only convert non-digit values to "Unknown" if they're not already valid PSA numbers
        # Valid PSA numbers are 3 digits between 101 and 708
        def is_valid_psa(x):
            try:
                psa_num = int(x)
                return 101 <= psa_num <= 708
            except (ValueError, TypeError):
                return False

        df.loc[~df["arrest_psa"].apply(is_valid_psa), "arrest_psa"] = "Unknown"

        print("\nPSA values after processing:")
        print(df["arrest_psa"].value_counts())
        print(
            f"Number of 2024 arrests after PSA processing: {len(df[df['year'] == 2024])}"
        )

    print(f"\nFinal number of 2024 arrests: {len(df[df['year'] == 2024])}")
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


def setup_plot(figsize=(12, 6)):
    """Set up common plot parameters."""
    plt.figure(figsize=figsize)
    plt.grid(True, linestyle="--", alpha=0.7)


def format_plot_axes(xlabel=None, ylabel=None, fontsize=14):
    """Format plot axes with common styling."""
    if xlabel:
        plt.xlabel(xlabel, fontsize=fontsize + 2)
    if ylabel:
        plt.ylabel(ylabel, fontsize=fontsize + 2)
    plt.xticks(fontsize=fontsize)
    plt.yticks(fontsize=fontsize)
    plt.legend(fontsize=18)
    plt.tight_layout()


def calculate_ward_level_changes(df):
    """Calculate changes in arrests by ward between 2023 and 2024."""
    ward_changes = []
    for ward in sorted(df["ward"].unique()):
        ward_df = df[df["ward"] == ward]
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
    # Return sorted by ward number
    return sorted(ward_changes, key=lambda x: x["ward"])


def main():
    """Main function to generate arrest report."""
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    print("\n=== Starting data processing ===")
    print("Reading and preprocessing data...")
    df = pd.read_csv("data/clean/arrest_data.csv.gz", low_memory=False)
    print(f"\nTotal rows in raw data: {len(df)}")
    print(f"2024 arrests in raw data: {len(df[df['date'].str.startswith('2024')])}")

    df = preprocess_data(df)
    print(f"\nTotal rows after preprocessing: {len(df)}")
    print(f"2024 arrests after preprocessing: {len(df[df['year'] == 2024])}")

    # Calculate statistics and print debug info
    print("\n=== Calculating statistics ===")
    stats = calculate_arrest_statistics(df)
    print("\nStatistics dictionary keys:")
    print(stats.keys())
    print("\nStatistics values:")
    for key, value in stats.items():
        if isinstance(value, (int, float, str)):
            print(f"{key}: {value}")
        else:
            print(f"{key}: {type(value)}")

    officers_df = pd.read_csv("data/clean/officers.csv")
    stops_df = None
    try:
        stops_df = preprocess_data(
            pd.read_csv("data/clean/stop_data.csv.gz", low_memory=False)
        )
    except FileNotFoundError:
        pass

    print("\n=== Generating report ===")
    report_anc_psa = generate_report(df, officers_df)
    with open(reports_dir / "arrest_report_anc_psa.md", "w") as f:
        f.write(report_anc_psa)

    print("\nReport generated successfully in the reports directory")


if __name__ == "__main__":
    main()

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
    "../data/clean/arrest_data_with_wards.csv.gz",
    parse_dates=["date", "year", "month_year"],
    low_memory=False,
)

# Create reports directory if it doesn't exist
reports_dir = Path("../reports/wards")
reports_dir.mkdir(parents=True, exist_ok=True)


def generate_ward_report(ward_num):
    """Generate a markdown report for a specific ward."""
    # Filter data for this ward
    ward_data = arrest_data[arrest_data.WARD == ward_num].copy()

    # Calculate basic statistics
    total_arrests = len(ward_data)
    arrests_per_year = ward_data.groupby(ward_data.year.dt.year).size()
    recent_arrests = len(ward_data[ward_data.year >= "2023-01-01"])

    # Calculate top categories
    top_categories = ward_data.category.value_counts().head(5)

    # Calculate monthly trends using month_year column that's already parsed
    monthly_trends = ward_data.groupby("month_year").size()

    # Create plots with optimized settings
    plt.figure(figsize=(12, 6))
    monthly_trends.plot(kind="line", title=f"Ward {ward_num} Monthly Arrests")
    plt.xlabel("Date")
    plt.ylabel("Number of Arrests")
    plt.xticks(rotation=45)
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
Ward {ward_num} has recorded {total_arrests:,} total arrests since 2013. In the past year (2023-2024), there have been {recent_arrests:,} arrests in this ward.

## Key Statistics
- Total Arrests: {total_arrests:,}
- Recent Arrests (2023-2024): {recent_arrests:,}
- Average Annual Arrests: {arrests_per_year.mean():.0f}

## Top Arrest Categories
"""
    for category, count in top_categories.items():
        description += f"- {category}: {count:,} arrests\n"

    description += f"""
## Monthly Trends
![Monthly Arrest Trends](ward_{ward_num}_monthly_trends.png)

## Category Distribution
![Top 10 Arrest Categories](ward_{ward_num}_categories.png)

## Analysis
"""

    # Add analysis based on data
    if recent_arrests > arrests_per_year.mean():
        description += f"Ward {ward_num} has seen an increase in arrest activity in recent years, with {recent_arrests:,} arrests in 2023-2024 compared to an average of {arrests_per_year.mean():.0f} arrests per year.\n"
    else:
        description += f"Ward {ward_num} has seen a decrease in arrest activity in recent years, with {recent_arrests:,} arrests in 2023-2024 compared to an average of {arrests_per_year.mean():.0f} arrests per year.\n"

    # Add category-specific analysis
    top_category = top_categories.index[0]
    description += f"The most common arrest category in this ward is {top_category}, with {top_categories[0]:,} arrests.\n"

    # Save the report
    with open(reports_dir / f"ward_{ward_num}_report.md", "w") as f:
        f.write(description)


# Get list of valid wards
valid_wards = sorted([ward for ward in arrest_data.WARD.unique() if pd.notna(ward)])
print(f"Generating reports for {len(valid_wards)} wards...")

# Generate reports for all wards with progress bar
for ward in tqdm(valid_wards, desc="Generating ward reports"):
    generate_ward_report(ward)

print("Ward reports have been generated in the reports/wards directory.")

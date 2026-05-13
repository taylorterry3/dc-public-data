#!/usr/bin/env python
"""Generate a focused PDF with 2023/2024/2025 arrest trend tables and charts.

No prose — just the data tables and visualizations.
Outputs: reports/arrest_trends_update.md + reports/images/trends_*.png
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.style.use("seaborn-v0_8")

REPORTS_DIR = Path("reports")
IMAGES_DIR = REPORTS_DIR / "images"
OUTPUT_MD = REPORTS_DIR / "arrest_trends_update.md"

YEARS = [2023, 2024, 2025]
CMP_YEAR1, CMP_YEAR2 = 2024, 2025  # The "change" columns compare these two years


def fmt_pct(v):
    if v == float("inf") or v == float("-inf") or pd.isna(v):
        return "N/A"
    v = int(round(v))
    return f"+{v}%" if v > 0 else f"{v}%"


def load_data():
    df = pd.read_csv("data/clean/arrest_data.csv.gz", low_memory=False)
    df["date"] = pd.to_datetime(df["date"])
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["ward"] = df["ward"].fillna(-1).astype(int)
    df = df[df["ward"] > 0]
    officers = pd.read_csv("data/clean/officers.csv")
    stops = pd.read_csv("data/clean/stop_data.csv.gz", low_memory=False)
    stops["date"] = pd.to_datetime(stops["date"], utc=True)
    stops["year"] = stops["date"].dt.year
    stops["month"] = stops["date"].dt.month
    return df, officers, stops


# ── Table 1: Arrests by ward ──────────────────────────────────────────────────

def ward_table(df):
    rows = []
    for ward in range(1, 9):
        wdf = df[df["ward"] == ward]
        counts = {y: len(wdf[wdf["year"] == y]) for y in YEARS}
        change = counts[CMP_YEAR2] - counts[CMP_YEAR1]
        pct = change / counts[CMP_YEAR1] * 100 if counts[CMP_YEAR1] else float("inf")
        rows.append((ward, counts, change, pct))

    lines = [
        f"| Ward | {YEARS[0]} | {YEARS[1]} | {YEARS[2]} | Change | % Change |",
        "|------|------:|------:|------:|--------:|--------:|",
    ]
    for ward, counts, change, pct in rows:
        lines.append(
            f"| {ward} | {counts[YEARS[0]]:,} | {counts[YEARS[1]]:,} | {counts[YEARS[2]]:,} | {change:+,} | {fmt_pct(pct)} |"
        )
    return "\n".join(lines)


# ── Table 2: Top category summary ─────────────────────────────────────────────

def top_category_table(df):
    top_cats = ["Traffic Violations", "Theft", "Narcotics", "Liquor Law Violations"]
    rows = []
    for cat in top_cats:
        counts = {y: len(df[(df["year"] == y) & (df["category"] == cat)]) for y in YEARS}
        change = counts[CMP_YEAR2] - counts[CMP_YEAR1]
        pct = change / counts[CMP_YEAR1] * 100 if counts[CMP_YEAR1] else float("inf")
        rows.append((cat, counts, change, pct))

    # All Other
    other_mask = ~df["category"].isin(top_cats)
    other_counts = {y: len(df[(df["year"] == y) & other_mask]) for y in YEARS}
    other_change = other_counts[CMP_YEAR2] - other_counts[CMP_YEAR1]
    other_pct = other_change / other_counts[CMP_YEAR1] * 100 if other_counts[CMP_YEAR1] else float("inf")
    rows.append(("All Other Categories", other_counts, other_change, other_pct))

    lines = [
        f"| Arrest Category | {YEARS[0]} | {YEARS[1]} | {YEARS[2]} | Change | % Change |",
        "|----------------|------:|------:|------:|--------:|--------:|",
    ]
    for cat, counts, change, pct in rows:
        lines.append(
            f"| {cat} | {counts[YEARS[0]]:,} | {counts[YEARS[1]]:,} | {counts[YEARS[2]]:,} | {change:+,} | {fmt_pct(pct)} |"
        )
    return "\n".join(lines)


# ── Table 3: Ward × category crosstab (% change CMP_YEAR1 → CMP_YEAR2) ───────

def ward_category_crosstab(df, year1, year2):
    top_cats = ["Traffic Violations", "Theft", "Narcotics", "Liquor Law Violations"]
    short = {
        "Traffic Violations": "Traffic",
        "Liquor Law Violations": "Liquor",
    }
    other_cats = set(df["category"].dropna().unique()) - set(top_cats)

    lines = [
        f"| Category | W1 | W2 | W3 | W4 | W5 | W6 | W7 | W8 |",
        "|:---------|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for cat in top_cats + ["Other"]:
        name = short.get(cat, cat)
        row = f"| {name}"
        for ward in range(1, 9):
            wdf = df[df["ward"] == ward]
            if cat == "Other":
                c1 = len(wdf[(wdf["year"] == year1) & wdf["category"].isin(other_cats)])
                c2 = len(wdf[(wdf["year"] == year2) & wdf["category"].isin(other_cats)])
            else:
                c1 = len(wdf[(wdf["year"] == year1) & (wdf["category"] == cat)])
                c2 = len(wdf[(wdf["year"] == year2) & (wdf["category"] == cat)])
            pct = (c2 - c1) / c1 * 100 if c1 else float("inf")
            row += f" | {fmt_pct(pct)}"
        lines.append(row + " |")
    return "\n".join(lines)


# ── Table 4: Full arrests by category ────────────────────────────────────────

def full_category_table(df):
    cats = sorted(c for c in df["category"].unique() if pd.notna(c))
    rows = []
    for cat in cats:
        counts = {y: len(df[(df["year"] == y) & (df["category"] == cat)]) for y in YEARS}
        change = counts[CMP_YEAR2] - counts[CMP_YEAR1]
        pct = change / counts[CMP_YEAR1] * 100 if counts[CMP_YEAR1] else float("inf")
        rows.append((cat, counts, change, pct))
    rows.sort(key=lambda r: -float("inf") if r[3] == float("inf") else r[3], reverse=True)

    lines = [
        f"| Arrest Category | {YEARS[0]} | {YEARS[1]} | {YEARS[2]} | Change | % Change |",
        "|----------------|------:|------:|------:|--------:|--------:|",
    ]
    for cat, counts, change, pct in rows:
        lines.append(
            f"| {cat} | {counts[YEARS[0]]:,} | {counts[YEARS[1]]:,} | {counts[YEARS[2]]:,} | {change:+,} | {fmt_pct(pct)} |"
        )
    return "\n".join(lines)


# ── Chart 1: Officer trends ───────────────────────────────────────────────────

def plot_officer_trends(df, officers, stops):
    fig, ax = plt.subplots(figsize=(12, 6))

    monthly_arrests = df.groupby(["year", "month"]).size().reset_index(name="arrests")
    monthly_arrests["date"] = pd.to_datetime(monthly_arrests[["year", "month"]].assign(day=1))

    officers_monthly = officers.copy()
    officers_monthly["date"] = pd.to_datetime(officers_monthly["year"].astype(str) + "-01-01")

    merged = pd.merge_asof(
        monthly_arrests.sort_values("date"),
        officers_monthly[["date", "officers"]].sort_values("date"),
        on="date", direction="backward",
    )
    merged["rate"] = merged["arrests"] / merged["officers"]

    monthly_stops = stops.groupby(["year", "month"]).size().reset_index(name="stops")
    monthly_stops["date"] = pd.to_datetime(monthly_stops[["year", "month"]].assign(day=1))
    monthly_stops = monthly_stops.iloc[1:]  # drop first partial month
    stops_merged = pd.merge_asof(
        monthly_stops.sort_values("date"),
        officers_monthly[["date", "officers"]].sort_values("date"),
        on="date", direction="backward",
    )
    stops_merged["rate"] = stops_merged["stops"] / stops_merged["officers"]

    ax.plot(stops_merged["date"], stops_merged["rate"], color="blue", label="Stops per Officer per Month", alpha=0.8)
    ax.plot(merged["date"], merged["rate"], color="red", label="Arrests per Officer per Month", alpha=0.8)

    years = sorted(df["year"].unique())
    ax.set_xticks([pd.Timestamp(f"{y}-01-01") for y in years])
    ax.set_xticklabels(years, fontsize=14)
    ax.tick_params(axis="y", labelsize=14)
    ax.set_xlabel("Year", fontsize=16)
    ax.set_ylabel("Monthly Rate", fontsize=16)
    ax.grid(True, linestyle="--", alpha=0.7)
    ax.legend(fontsize=16)
    plt.tight_layout()
    path = IMAGES_DIR / "trends_officer_rates.png"
    plt.savefig(path, dpi=100)
    plt.close()
    return path.name


# ── Chart 2: Horizontal bar chart by category ────────────────────────────────

def plot_category_bars(df):
    cats = sorted(c for c in df["category"].unique() if pd.notna(c))
    colors = ["#66c2a5", "#fc8d62", "#8da0cb"]  # 3 distinct colors

    counts = {
        y: df[df["year"] == y]["category"].value_counts().reindex(cats).fillna(0)
        for y in YEARS
    }

    y_pos = np.arange(len(cats))
    width = 0.25

    fig, ax = plt.subplots(figsize=(12, 11))
    for i, (year, color) in enumerate(zip(YEARS, colors)):
        ax.barh(y_pos + (i - 1) * width, counts[year], width, label=str(year), color=color)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(cats, fontsize=13)
    ax.tick_params(axis="x", labelsize=13)
    ax.set_xlabel("Number of Arrests", fontsize=15)
    ax.set_title("Citywide Arrests by Category", fontsize=18, fontweight="bold")
    ax.legend(fontsize=16)
    ax.invert_yaxis()
    plt.tight_layout()
    path = IMAGES_DIR / "trends_categories.png"
    plt.savefig(path, dpi=100)
    plt.close()
    return path.name


# ── Assemble markdown ─────────────────────────────────────────────────────────

def main():
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    print("Loading data...")
    df, officers, stops = load_data()

    print("Generating charts...")
    officer_chart = plot_officer_trends(df, officers, stops)
    category_chart = plot_category_bars(df)

    print("Building report...")
    md = []

    md.append("# Adult Arrest Trends: 2023–2025\n")

    md.append("## Arrests by Ward\n")
    md.append(ward_table(df))
    md.append("\n\\newpage\n")

    md.append("## Top Category Changes\n")
    md.append(top_category_table(df))
    md.append("\n\\newpage\n")

    md.append(f"## Category Change by Ward (2023–2025)\n")
    md.append("\\small")
    md.append(ward_category_crosstab(df, 2023, 2025))
    md.append("\\normalsize\n")
    md.append(f"## Category Change by Ward (2023–2024)\n")
    md.append("\\small")
    md.append(ward_category_crosstab(df, 2023, 2024))
    md.append("\\normalsize")
    md.append("\n## Arrests and Stops per Officer per Month\n")
    md.append(f"![](images/{officer_chart})\n")
    md.append("\n\\newpage\n")

    md.append("## Arrests by Category\n")
    md.append(full_category_table(df))
    md.append("\n\\newpage\n")

    md.append(f"![](images/{category_chart})\n")

    OUTPUT_MD.write_text("\n".join(md))
    print(f"Wrote {OUTPUT_MD}")
    print("Now run:  bash scripts/render_pdfs.sh")


if __name__ == "__main__":
    main()

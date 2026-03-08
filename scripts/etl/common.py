"""Shared transformation utilities used across all ETL pipelines."""

import pandas as pd


def data_cleanup(df: pd.DataFrame, date_col: str) -> pd.DataFrame:
    """Parse dates and create convenience fields (month_year, year)."""
    df["date"] = pd.to_datetime(df[date_col], format="mixed", utc=True)
    df["month_year"] = df.date.dt.strftime("%Y-%m")
    if "YEAR" not in df.columns:
        df["year"] = df.date.dt.year
    df.columns = [c.lower() for c in df.columns]

    if "arrest_psa" in df.columns:
        df["arrest_psa"] = df["arrest_psa"].astype(str)
        df.loc[df["arrest_psa"].str.match(r"^\d+\.0$"), "arrest_psa"] = df.loc[
            df["arrest_psa"].str.match(r"^\d+\.0$"), "arrest_psa"
        ].str.replace(r"\.0$", "", regex=True)

    return df


def arrest_category_cleanup(df: pd.DataFrame) -> pd.DataFrame:
    """Fix corrupted category strings in pre-2017 arrest data.

    Data through 2017 has "Na" dropped from strings in the category field.
    Also rolls up a few miscategorized values in Release Violations and
    Fraud/Financial categories.
    """
    fixes = {
        " rcotics": "Narcotics",
        "Fraud and Fi ncial Crimes": "Fraud and Financial Crimes",
        "Fraud and Financial Crimes (Coun)": "Fraud and Financial Crimes",
        "Fraud and Financial Crimes (Forg)": "Fraud and Financial Crimes",
        "Fraud and Financial Crimes (Frau)": "Fraud and Financial Crimes",
        "Kid pping": "Kidnapping",
        "Release Violations/Fugitive (Fug)": "Release Violations/Fugitive",
        "Release Violations/Fugitive (Warr)": "Release Violations/Fugitive",
        "Release Violations": "Release Violations/Fugitive",
    }
    df["category"] = df["category"].apply(lambda x: fixes.get(x, x))
    return df

"""Unit tests for scripts.etl.common transforms."""

import pandas as pd
import pytest

from scripts.etl.common import arrest_category_cleanup, data_cleanup


class TestDataCleanup:
    def test_parses_date_column(self):
        df = pd.DataFrame({"DATE_": ["2024-01-15 10:30:00", "2023-06-01 00:00:00"]})
        result = data_cleanup(df.copy(), "DATE_")
        assert pd.api.types.is_datetime64_any_dtype(result["date"])

    def test_creates_month_year(self):
        df = pd.DataFrame({"DATE_": ["2024-03-15"]})
        result = data_cleanup(df.copy(), "DATE_")
        assert result["month_year"].iloc[0] == "2024-03"

    def test_creates_year_when_missing(self):
        df = pd.DataFrame({"DATE_": ["2024-03-15"]})
        result = data_cleanup(df.copy(), "DATE_")
        assert result["year"].iloc[0] == 2024

    def test_does_not_overwrite_existing_year_column(self):
        df = pd.DataFrame({"DATE_": ["2024-03-15"], "YEAR": [2024]})
        result = data_cleanup(df.copy(), "DATE_")
        # year should not be duplicated — original YEAR column lowercased to 'year'
        assert "year" in result.columns

    def test_lowercases_all_columns(self):
        df = pd.DataFrame({"DATE_": ["2024-01-01"], "ARREST_PSA": ["101"]})
        result = data_cleanup(df.copy(), "DATE_")
        assert all(c == c.lower() for c in result.columns)

    def test_normalizes_psa_float_strings(self):
        df = pd.DataFrame({"DATE_": ["2024-01-01"], "ARREST_PSA": ["101.0"]})
        result = data_cleanup(df.copy(), "DATE_")
        assert result["arrest_psa"].iloc[0] == "101"

    def test_leaves_clean_psa_strings_unchanged(self):
        df = pd.DataFrame({"DATE_": ["2024-01-01"], "ARREST_PSA": ["307"]})
        result = data_cleanup(df.copy(), "DATE_")
        assert result["arrest_psa"].iloc[0] == "307"


class TestArrestCategoryCleanup:
    def test_fixes_narcotics_corruption(self):
        df = pd.DataFrame({"category": [" rcotics"]})
        result = arrest_category_cleanup(df.copy())
        assert result["category"].iloc[0] == "Narcotics"

    def test_fixes_fraud_variants(self):
        variants = [
            "Fraud and Fi ncial Crimes",
            "Fraud and Financial Crimes (Coun)",
            "Fraud and Financial Crimes (Forg)",
            "Fraud and Financial Crimes (Frau)",
        ]
        for variant in variants:
            df = pd.DataFrame({"category": [variant]})
            result = arrest_category_cleanup(df.copy())
            assert result["category"].iloc[0] == "Fraud and Financial Crimes", variant

    def test_fixes_kidnapping_corruption(self):
        df = pd.DataFrame({"category": ["Kid pping"]})
        result = arrest_category_cleanup(df.copy())
        assert result["category"].iloc[0] == "Kidnapping"

    def test_normalizes_release_violations(self):
        variants = [
            "Release Violations/Fugitive (Fug)",
            "Release Violations/Fugitive (Warr)",
            "Release Violations",
        ]
        for variant in variants:
            df = pd.DataFrame({"category": [variant]})
            result = arrest_category_cleanup(df.copy())
            assert result["category"].iloc[0] == "Release Violations/Fugitive", variant

    def test_leaves_clean_categories_unchanged(self):
        clean = ["Theft", "Assault", "Narcotics", "Weapon Violations"]
        df = pd.DataFrame({"category": clean})
        result = arrest_category_cleanup(df.copy())
        assert result["category"].tolist() == clean

    def test_handles_mixed_clean_and_corrupt(self):
        df = pd.DataFrame({"category": ["Theft", " rcotics", "Assault", "Kid pping"]})
        result = arrest_category_cleanup(df.copy())
        assert result["category"].tolist() == ["Theft", "Narcotics", "Assault", "Kidnapping"]

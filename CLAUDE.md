# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

ETL scripts and analysis notebooks for Washington, DC public data — policing, crime, and 311 requests. Data flows: raw CSVs → ETL → cleaned gzip CSVs → report generation → markdown/HTML/PDF outputs.

The repo is being actively developed toward three goals:

1. **ETL modernization** — Break the monolithic `ETL.py` and `generate_ward_reports.py` into modular, per-dataset pipelines so individual datasets can be updated and reprocessed independently. Improve test coverage of ETL logic.

2. **Public data visualization site** — Replace the current notebook/PDF/HTML report workflow with a deployable web application. The site should support browsing data by topic and geography (Ward, ANC, SMD), include maps and charts, and have a front page with featured analysis and blog-style content. It should be architected to support many additional data topics over time. Stack preference: Python backend, appropriate JS for charts and maps on the frontend.

3. **Automated data refresh** — Check DC Open Data (and other sources) for new data, run ETL, and push updated data to the production site on a schedule.

### Architecture Decisions Still Open

**Hosting/data platform:** The leading options are:
- **Google Cloud Platform end-to-end**: host the site on Cloud Run or App Engine, store cleaned data in BigQuery (which can be made publicly queryable), use GCS for raw file storage. Good for making datasets independently public.
- **Supabase + separate BigQuery**: host the app on Supabase (Postgres + auth + storage), publish datasets separately to BigQuery for public access. More portable, less Google lock-in.

A primarily Python backend is preferred. BigQuery is attractive for making datasets publicly accessible independent of the website. No final decision has been made — evaluate tradeoffs when beginning the site build.

## Environment

The project uses [uv](https://docs.astral.sh/uv/) for package and environment management on Python 3.14. `pyproject.toml` is the source of truth for dependencies — do not edit `requirements.txt` (kept only as a historical reference). Add new dependencies with `uv add <package>`.

The old pyenv virtualenv may still be activated in your shell, producing a harmless `VIRTUAL_ENV does not match` warning from uv — this can be ignored.

## Common Commands

All commands should be run from the project root via `uv run`.

```bash
# Run the full ETL pipeline (reads from data/raw/, writes to data/clean/)
uv run python scripts/ETL.py

# Generate arrest ward reports (reads from data/clean/, writes to reports/)
uv run python scripts/generate_ward_reports.py

# Convert the arrest report markdown to HTML
uv run python scripts/render_reports.py

# Convert to PDF (requires pandoc)
bash scripts/render_pdfs.sh

# Run all tests
uv run pytest

# Run a single test file
uv run pytest tests/unit/test_data_completeness.py

# Run a single test
uv run pytest tests/unit/test_data_completeness.py::test_years_completeness

# Lint
uv run ruff check scripts/ tests/

# Add a new dependency
uv add <package>
uv add --dev <package>   # dev-only (testing, linting)
```

## Architecture

### Data Pipeline

1. **`data/raw/`** — Source files downloaded manually from DC Open Data (see `data/raw/sources.md` for URLs)
2. **`scripts/ETL.py`** — Reads raw data, performs spatial joins (ward/SMD/ANC via geopandas), fixes historical data quality issues, writes gzip-compressed CSVs to `data/clean/`
3. **`scripts/generate_ward_reports.py`** — Reads cleaned data, produces `reports/arrest_report.md` with year-over-year comparison tables by ward/district/ANC/PSA
4. **`scripts/render_reports.py` / `render_pdfs.sh`** — Convert the markdown report to HTML and PDF

### Key Data Files

- **`data/clean/arrest_data.csv.gz`** — Cleaned arrests with spatial enrichment (ward, SMD, ANC columns added via geopandas sjoin)
- **`data/clean/stop_data.csv.gz`** — Merged stop data (two source files joined on common columns, deduped on `ccn_anonymized`)
- **`data/clean/311_data_part_{0,1,2}.csv.gz`** — 311 service requests split into 3 parts due to size
- **`data/clean/incident_data.csv.gz`** / **`incident_data_all.csv.gz`** — Crime incident data from two different sources

### Spatial Enrichment (ETL.py)

Arrest lat/lon coordinates are spatially joined against:
- `data/raw/Wards_from_2022.geojson` → adds `ward`, `name` columns
- `data/raw/Single_Member_District_from_2023.geojson` → adds `smd_id`, `anc_id` columns

All coordinates use EPSG:4326. Rows with no ward match are dropped.

### Data Quality Notes

- Pre-2017 arrest data has corrupted `category` values (missing "Na" characters) — `arrest_category_cleanup()` in ETL.py corrects these
- Stop data is merged from two year-range files; only common columns are kept
- The `ccn_anonymized` field is used for deduplication in stop data
- PSA values are normalized to strings (stripping `.0` float artifacts)

### Testing

Tests live in `tests/` with pytest fixtures in `tests/conftest.py`. Most fixtures use synthetic/mock data rather than the actual cleaned CSVs. The test suite was written as an AI experiment and coverage of core ETL logic is a known gap to fill.

```
tests/
├── conftest.py                    # Shared fixtures (synthetic arrest_data, officers_data)
├── test_arrest_report.py          # Report content validation
├── unit/test_data_completeness.py # Column/ward/year completeness checks
└── integration/test_report_generation.py
```

## Planned Work

### ETL Modularization
- Refactor `ETL.py` into per-dataset modules (arrests, stops, incidents, 311) that can each be run independently
- Large functions in `generate_ward_reports.py` should be broken up similarly
- Each module should be independently testable with good unit test coverage of transformation logic
- Goal: adding a new data topic should not require touching existing dataset code

### Web Application
- Build a deployable site to replace the current notebook/HTML/PDF workflow
- Must support geographic navigation: Ward, ANC, SMD
- Must support topic navigation across all current and future datasets
- Front page with featured analysis and blog-style posts
- Extensive charts (likely Plotly or similar Python-friendly library) and maps (Leaflet or Mapbox)
- Notebooks are the reference for what analyses and visualizations should be reproduced

### Automated Data Refresh
- Detect and download new data from DC Open Data portal and other sources
- Run relevant ETL modules on new data
- Push updated data to production site
- Details TBD; flesh out after ETL modularization is complete

#!/usr/bin/env python
"""ETL orchestrator for DC public data.

Run all pipelines:
    uv run python scripts/ETL.py

Run a single pipeline:
    uv run python scripts/ETL.py --only arrests
    uv run python scripts/ETL.py --only stops
    uv run python scripts/ETL.py --only incidents
    uv run python scripts/ETL.py --only 311
"""

import argparse

import scripts.etl.arrests as arrests_etl
import scripts.etl.incidents as incidents_etl
import scripts.etl.service_311 as service_311_etl
import scripts.etl.stops as stops_etl

PIPELINES = {
    "arrests": arrests_etl.run,
    "stops": stops_etl.run,
    "incidents": incidents_etl.run,
    "311": service_311_etl.run,
}


def main():
    parser = argparse.ArgumentParser(description="Run DC public data ETL pipelines")
    parser.add_argument(
        "--only",
        choices=list(PIPELINES.keys()),
        help="Run only one pipeline instead of all",
    )
    args = parser.parse_args()

    targets = [args.only] if args.only else list(PIPELINES.keys())
    for name in targets:
        print(f"\n{'=' * 50}")
        print(f"Running {name} pipeline...")
        print("=" * 50)
        PIPELINES[name]()


if __name__ == "__main__":
    main()

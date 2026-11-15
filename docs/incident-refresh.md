# Annual incident refresh operations

The workflow downloads annual crime incident data from the official MPD ArcGIS service, validates it, runs annual incident ETL, and proposes raw and cleaned files in one review PR. Crime Cards exports, other topics, reports, and production publishing are separate work.

## Running

After the workflow is merged into `main`, use **Actions → Refresh annual crime incidents → Run workflow**. Select `full_history` to force all represented years to download. The scheduled run is intended for 9 a.m. America/New_York; GitHub may delay scheduled jobs. Two UTC slots and an offset gate preserve that local time across daylight saving changes.

The first successful run in each calendar month downloads all years represented in the repo, plus newly published years. A monthly Actions cache marker avoids repeated historical downloads; cache misses/evictions safely cause another full sweep. Later runs download the current and previous year and any missing published years since the earliest represented year. A missing current-year source is visible in the summary; a missing previously accepted year fails the run.

No reliable data-edit watermark has been verified, so metadata-based historical skipping is not enabled. See the [source research](research/incident-source-contract.md).

For a local refresh against a clean checkout:

```sh
uv run python -m scripts.refresh_incidents --summary /tmp/incident-refresh.md
# Include all historical years:
uv run python -m scripts.refresh_incidents --full-history --summary /tmp/incident-refresh.md
```

Local commands write validated raw and annual cleaned files in the checkout; inspect the diff before committing. They do not create branches or PRs. Without a monthly cache marker, local runs use recent years unless `--full-history` is set.

## Downloads and validation

Layers are discovered by exact year-specific names rather than inferred numeric IDs. The downloader obtains the full source OBJECTID list, retrieves bounded batches, reconciles each batch, then checks the full ID list again. Truncation, missing/duplicate IDs, and changed ID snapshots fail the run. Source changes that preserve the ID list cannot be ruled out; this endpoint does not offer a transactional snapshot.

Required columns and values, dates, report-year membership, unique OBJECTIDs within each annual export, and counts against accepted `main` files are checked. CCN remains a string and is allowed to repeat. Incident start dates may precede the report year; missing start/end dates are allowed, as in the accepted source files. Empty exports and count decreases fail closed, including legitimate publisher deletions. There is no bypass flag: investigate and prepare a separately reviewed manual correction.

REST dates are serialized in UTC. Source geometry supplies the existing X/Y columns in EPSG:26985. Identifiers remain strings when reading CSVs for ETL. The first export may have formatting-only differences from old portal CSVs. Thereafter deterministic row ordering, CSV formatting and gzip timestamps prevent identical downloads from generating commits.

All attempted years validate before annual ETL runs and checkout files are replaced. The Crime Cards cleaned file is not regenerated. Source URLs, retrieval time, row counts, maximum report dates and export hashes appear in the run summary and proposed PR.

## Review and failure behavior

The bot owns `automation/annual-incidents`. Successful runs update its open PR rather than creating a new PR every day. Do manual corrections on a separate branch: bot updates may replace edits on its own branch.

While a PR is open, its pending raw/cleaned files are restored before refreshing recent years, preserving historical corrections awaiting review. Count checks still compare against a separate snapshot of accepted `main`, not the bot branch. A failed download/validation/ETL never reaches the PR action, so the remote PR is left unchanged. The temporary Actions checkout can be discarded on failure.

The PR includes only `data/raw/Crime_Incidents_in_*.csv` and `data/clean/incident_data.csv.gz`. Review and merge it manually. There is no auto-merge or production deployment. No new failure issues are created: inspect the failed Actions step and run summary. Cached sweep markers are saved only after successful download, validation and PR handling.

## GitHub setup

The workflow uses the repository `GITHUB_TOKEN` with `contents: write` and `pull-requests: write`. Under **Settings → Actions → General → Workflow permissions**, enable **Allow GitHub Actions to create and approve pull requests**. Organization policy can prevent enabling it; no personal token is needed by this implementation. The workflow does not approve PRs despite the setting's name.

Source code and unit tests should be reviewed before merging the workflow into `main`, where scheduled workflows run. Actions-created PRs may require approval for downstream workflows, depending on GitHub policy. This workflow does not depend on Claude reviews to validate downloads.

Public source requests have bounded retries and timeouts. A first monthly sweep makes more requests than a daily refresh and may encounter source outages; rerun after investigation. A successful run proves export validity against these checks, not the publisher's completeness or timeliness.

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

Required columns and values, dates, report-year membership, unique OBJECTIDs within each annual export, and export completeness are checked. CCN remains a string and is allowed to repeat. Incident start dates may precede the report year; missing start/end dates are allowed, as in the accepted source files. Empty or incomplete exports still fail closed. A lower raw count is allowed: records absent from a complete snapshot are retained in the history dataset and flagged absent. PR summaries show source, retained, absent and archived-version counts for review.

REST dates are serialized in UTC. Source geometry supplies the existing X/Y columns in EPSG:26985. Identifiers remain strings when reading CSVs for ETL. The first export may have formatting-only differences from old portal CSVs. Thereafter deterministic row ordering, CSV formatting and gzip timestamps prevent identical downloads from generating commits.

All attempted years validate before annual ETL runs and checkout files are replaced. The Crime Cards cleaned file is not regenerated. The Actions summary describes the latest download run. The PR description is rebuilt from every pending file against accepted `main`, including preserved historical years, with accepted/candidate row counts, source URLs, maximum report dates and file hashes. Report-generation time does not imply historical files were downloaded again.

## Review and failure behavior

The bot owns `automation/annual-incidents`. Successful runs update its open PR rather than creating a new PR every day. Do manual corrections on a separate branch: bot updates may replace edits on its own branch.

While a PR is open, its branch is merged into current `main` in the disposable checkout before refreshing recent years. Full Git history supplies the common ancestor. Conflicts stop the run before publication; nonconflicting accepted corrections and pending updates are preserved. The merged diff is left uncommitted against `main` for the PR action, and pending raw changes trigger a cleaned-data rebuild. Pending annual files still receive schema and date validation. The accepted snapshot seeds initial history, so a smaller pending raw snapshot cannot discard accepted records during migration. Merged historical raw corrections are reconciled with unknown observation dates; they do not fabricate a fresh sighting. A failed download/validation/ETL never reaches the PR action, so the remote PR is left unchanged. The temporary Actions checkout can be discarded on failure.

The PR includes `data/raw/Crime_Incidents_in_*.csv`, `data/clean/incident_data.csv.gz`, and `data/history/incidents/`. Review and merge it manually. There is no auto-merge or production deployment. No new failure issues are created: inspect the failed Actions step and run summary. Cached sweep markers are saved only after successful download, validation and PR handling.

## GitHub setup

The workflow uses the repository `GITHUB_TOKEN` with `contents: write` and `pull-requests: write`. Under **Settings → Actions → General → Workflow permissions**, enable **Allow GitHub Actions to create and approve pull requests**. Organization policy can prevent enabling it; no personal token is needed by this implementation. The workflow does not approve PRs despite the setting's name.

Source code and unit tests should be reviewed before merging the workflow into `main`, where scheduled workflows run. Actions-created PRs may require approval for downstream workflows, depending on GitHub policy. This workflow does not depend on Claude reviews to validate downloads.

Public source requests have bounded retries and timeouts. A first monthly sweep makes more requests than a daily refresh and may encounter source outages; rerun after investigation. A successful run proves export validity against these checks, not the publisher's completeness or timeliness.


## Retained records and version history

For each downloaded year, `data/history/incidents/<year>/current.csv.gz` contains one current version of every retained occurrence. `versions.csv.gz` archives prior values when business fields change. Raw annual files remain faithful source snapshots. The ordinary annual ETL also reads this history, so rerunning `scripts.ETL --only incidents` preserves retained records.

History payload values are preserved as strings. Metadata columns are:

| Column | Meaning |
| --- | --- |
| `record_id` | Project-owned occurrence identifier, scoped by annual report year |
| `first_seen_on`, `last_seen_on` | First and last successful complete refresh dates observing this record |
| `present_in_latest_source` | `true` or `false` for that year's latest complete snapshot; blank means unobserved |
| `version` | Monotonic version number within the retained record |
| `version_first_seen_on`, `version_last_seen_on` | Observation dates for the current payload values |
| `baseline_imported_on` | Date the legacy accepted row was imported, when known; not a source observation |
| `superseded_on` | Date a replacement was observed; only present in the archive |

Observation dates use America/New_York and describe successful acquisitions, not incident dates. On migration, existing accepted rows have unknown observation dates until actually seen. A legacy row already absent from the current source retains unknown first/last dates. A missing record keeps its last-seen date; a reappearance reconnects its identity where matching is unambiguous. Skipped years retain their dates. Successful next-day observations advance last-seen dates even when the source data is unchanged, so history-only review PR changes are expected. Failed runs publish neither observations nor dates.

Matching first pairs equivalent business payloads within the same year and CCN, then unambiguous offense/method/report-date/start-date/block anchors, then a single remaining old/new pair within the CCN. Publisher OBJECTID/OCTO_RECORD_ID and derived X/Y do not prove longitudinal identity. Formatting is normalized for comparison only (dates in UTC, numeric coordinate precision to six decimals, repeated/outer block-address whitespace collapsed); payload values stay intact in storage. Distinct coordinate changes outside that precision are revisions. Publisher-ID-only changes update the current payload without creating a business version. Indistinguishable duplicates retain multiplicity; their individual continuity is unknowable, so equivalent occurrences use a deterministic tie-breaker. Multiple unmatched non-equivalent candidates fail for manual mapping rather than silently coalescing records. CCN changes and moves between annual report years are conservatively treated as a disappearance plus an addition.

The cleaned annual dataset uses only current retained versions, with metadata columns, and excludes the version archive. Default totals therefore include retained absent records. Filter `present_in_latest_source == true` for the current published subset; a blank value denotes a year that has not yet been observed by this system. Consumers must choose their intended population explicitly.

The initial 2014 comparison on 2026-11-15 found 38,407 source rows versus 38,486 accepted rows: 105 missing and 26 additions. Retention yields 38,512 records. Many payloads have geographical revisions; initial version archives can consequently be large. Matching decisions and source disappearance are observations, not proof of why a publisher removed or changed a record.

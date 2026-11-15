# Automated data updates

Status: design confirmed; implementation complete locally. Deployment awaits review and merge of the workflow into main.

## Agreed scope

- First milestone: automate source downloads and ETL; production publishing comes later.
- First dataset: crime incidents. Arrests, stops, and 311 follow after the workflow is established.
- Review: submit refreshed data as a pull request for human review before replacing accepted data.
- First source: annual DC Open Data crime-incident files; automate the separate Crime Cards export in a later phase.
- Execution environment: GitHub Actions.
- Update PR contents: changed raw source files and their cleaned output; report regeneration is deferred.
- Schedule: daily at 9 a.m. America/New_York, with a manual run option. This is a polling policy, not a guarantee of source freshness. See [cadence research](research/crime-data-update-cadence.md).
- PR lifecycle: update one existing refresh PR while it remains open.
- Historical coverage: include corrections to years already represented in the repo and discover newly available years.
- Validation: fail the run on download failures, missing required columns, duplicate record identifiers, or record-count decreases relative to accepted data. Preserve accepted data; legitimate deletions require explicit review.
- Historical checking: use lightweight source-change checks where supported and download only changed years. Where reliable change detection is unavailable, download current and previous years daily and sweep historical years monthly.
- Failure visibility: use GitHub Actions failed-run status and a run summary identifying the failed source or validation. Do not automatically create failure issues.
- Legitimate deletions: stop for a manual correction; the first version has no automated validation bypass.
- Partial failures: if any attempted year fails download or validation, fail the entire run and leave the refresh PR unchanged. Stage changes separately until every attempted year passes.

## Current behavior

The incident pipeline reads local annual crime-incident files and a separate Crime Cards export. These produce separate cleaned outputs. Existing GitHub workflows handle Claude interactions and reviews; none download or refresh data.

## Source findings

See [source contract research](research/incident-source-contract.md). Discover annual layers by name rather than guessing layer IDs. A reliable data-edit watermark has not been verified; retain the monthly historical sweep. Verify download transport, complete exports, and row identifier behavior before enabling scheduled writes. CCN is not guaranteed unique and must not be used alone for duplicate-record rejection.

## Implementation verification

- Live service discovery found 19 annual layers; a complete 2026 export passed ID-list reconciliation and validation (19,270 rows on 2026-11-15).
- Offline validation/staging tests cover truncated exports, source ID changes, duplicates, count decreases, new years, monthly fallback, no-op runs, pending historical updates, and nullable incident dates.
- A disposable pandas-only environment successfully rebuilt 35,939 cleaned rows from accepted 2025 data and the live 2026 export.
- Workflow syntax passed actionlint. Scheduled execution and remote PR creation remain to be exercised after merge; source validation intentionally fails closed on unexpected historical differences.
- The repository Actions PR-creation setting is enabled; default workflow token permissions remain read-only. This workflow explicitly requests contents and PR write access.

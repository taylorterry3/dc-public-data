# Full local annual incident audit

Snapshot acquired 2026-11-16 UTC (2026-11-15 Washington time). The [source manifest](incident-audit-source-manifest.json) records each official layer URL, retrieval time, row count and SHA-256. Accepted-file baseline: commit `7422c32`.

## Scope and reproduced failures

Downloaded all 19 published annual layers, 2008–2026: **605,795 source rows**. Each download used the production completeness checks. The production refresh scope begins in 2014, so full replay covers **13 years and 404,065 source rows**. Older downloaded years were validated but were not silently added to the accepted scope.

The preflight examined every duplicate-CCN group in scope: **104 groups**. It exposed four failures at once:

| Year | CCN | Accepted block | Updated block |
| --- | --- | --- | --- |
| 2018 | 18067093 | 100–146 Wayne Place SE | 100–147 Wayne Place SE |
| 2020 | 20041985 | 4400–4499 Iowa Avenue NW | 4300–4399 Iowa Avenue NW |
| 2020 | 20074317 | 2400–2500 Martin Luther King Jr Avenue SE | 2400–2499 Martin Luther King Jr Avenue SE |
| 2021 | 21042347 | 4200–4351 4th Street SE | 4200–4232 4th Street SE |

Each group has two business-equivalent occurrences on both sides. Complaint/year, offense, method, report time, start time and end time agree, while block ranges and coordinates were corrected. The original full refresh reproduced the first failure in 2018 after passing 2014–2017. The captured accepted/source rows and provenance are in `tests/fixtures/incident_address_corrections.json`.

## Fix

After exact business and original location/time matching, permit matching on offense, method, report time and the complete start/end interval. Both sides must still consist of equivalent candidate payloads within each group. This preserves indistinguishable occurrence multiplicity without matching distinct competing candidates. The revised addresses and coordinates remain actual archived revisions, not formatting normalization. If both location and incident interval change for multiple candidates, reconciliation still fails for investigation.

All four captured cases pass in both incoming orders. Existing competing-incoming guards still reject ambiguity. The complete 104-group preflight now reports zero issues.

## Full production replay

The real refresh, retained-history generation, annual ETL and PR reporting passed every year against the frozen exports in a disposable data tree. Accepted files in the repository were not changed.

| Year | Current source rows | Retained records | Absent from source | Archived versions |
| --- | --- | --- | --- | --- |
| 2014 | 38,407 | 38,512 | 105 | 38,294 |
| 2015 | 37,181 | 37,336 | 155 | 36,989 |
| 2016 | 37,189 | 37,274 | 85 | 37,061 |
| 2017 | 33,094 | 33,157 | 63 | 32,984 |
| 2018 | 33,846 | 33,850 | 4 | 32,964 |
| 2019 | 33,968 | 33,971 | 3 | 32,839 |
| 2020 | 27,932 | 27,936 | 4 | 27,229 |
| 2021 | 28,320 | 28,368 | 48 | 27,595 |
| 2022 | 27,162 | 27,266 | 104 | 26,422 |
| 2023 | 34,236 | 34,253 | 17 | 118 |
| 2024 | 29,304 | 29,343 | 39 | 43 |
| 2025 | 24,156 | 24,211 | 55 | 74 |
| 2026 | 19,270 | 19,270 | 0 | 0 |
| **Total** | **404,065** | **404,747** | **682** | **292,612** |

Initial archives are large because accepted historical files predate widespread geographical revisions. Versions are separate from incident totals. These results establish behavior for this frozen snapshot, not a guarantee about future publisher revisions or transactional consistency of live exports.

For repeatable commands, cache behavior and generated artifacts, see [local audit operations](../incident-refresh.md#full-local-audit-before-running-actions).


## Repeat verification

A second full refresh against the generated history and identical frozen files completed all 13 years with **zero changed files**. Additional checks confirmed exact raw-export bytes, published-subset counts, no loss of accepted occurrences, archive count/version-counter consistency, unique cleaned record IDs, and the totals above. The unit suite now has **74 passing tests**; Ruff and whitespace checks pass.

The local artifacts are retained under ignored `.cache/incident-audit-full/`:

- `manifest.json`: all 19 source snapshots and hashes.
- `audit.json`: complete 104-group preflight, zero remaining issues.
- `replay-fixed/`: full generated raw/history/cleaned data tree.
- `replay-fixed-result.json`: first successful refresh results.
- `replay-fixed-verification.json`: repeat-run results and reconciled totals.
- `replay-fixed-pr.md` / `replay-fixed-summary.md`: rendered reports.

The earlier unsuccessful `replay/` directory is preserved as well. No bulk snapshots or generated datasets are committed. To repeat the verification locally:

```sh
uv run python -m scripts.audit_incidents --cache-dir .cache/incident-audit-full --verify-replay --replay-name replay-fixed
```

GitHub PR-creation and branch-update behavior are outside this offline data replay. This audit removes the known historical-data blockers; it does not assert that future live source snapshots cannot introduce new cases.


## Review hardening

Greptile identified three gaps in the audit tool; all were reproduced with failing regressions and fixed:

- Preflight now uses retained candidates, including absent records, and passes current/archived metadata to reconciliation. Preflight against the full generated history passed **108 groups** with zero issues; the original accepted-raw preflight still passes its 104 groups.
- Resume retains the saved inventory and rejects mapping changes (including added years) before changing files. Completed frozen exports are never silently redownloaded after corruption. A full 19-export resume reused all files with zero downloads and byte-identical manifest contents.
- Retention checks use accepted record IDs when history exists. Initial imports require globally distinct retained-record witnesses for every accepted canonical payload occurrence, including duplicates, across current and archived values. One record's several versions cannot stand in for several accepted occurrences, even when their payloads differ. The checker allows valid converging revisions by reassigning witnesses when needed.

The stronger initial-import proof passed all 13 years, covering **377,477 accepted occurrences**; 2026 has no preexisting accepted rows. A further complete repeat preserved all **404,747 retained IDs**, reconciled the same totals, and produced zero file changes. Evidence is retained in `.cache/incident-audit-full/replay-fixed-retention-proof.json`, `audit-retained-history.json`, and `replay-fixed-verification.json`. The revised unit suite has **74 passing tests**; Ruff and whitespace checks pass. No accepted datasets changed.

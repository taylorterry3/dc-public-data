# Crime data update cadence

Researched 2026-11-15. Scope: distinguish Crime Cards from the Open Data DC annual Crime Incidents downloads used by the initial ingestion implementation. Only government-published information and the official application's own help text support the findings below.

## Confirmed: Crime Cards

- The current application's FAQ, under **Why can't I see today's incidents?**, says Crime Cards is built on OpenDataDC and is **“refreshed once a day in the early morning hours.”** It explains that incidents occurring within the last 24 hours may not yet appear. This is an explicit cadence statement, not an inference from an update timestamp. The FAQ is present in the [current official application bundle](https://crimecards.dc.gov/main.ff606deacb1bcd0e6575.js), linked by the [Crime Cards page](https://crimecards.dc.gov/). The bundle was retrieved directly on the research date because the ordinary HTML is an application shell and search extraction omits collapsed FAQ answers.
- That FAQ clarifies the cutoff as **11:59:59 pm yesterday**. The application's introductory help says its statistics use the date an offense was reported to MPD, rather than necessarily the date it occurred. [Official application/help text](https://crimecards.dc.gov/main.ff606deacb1bcd0e6575.js). [OCTO's service description](https://octo.dc.gov/service/dc-crime-cards) independently identifies Report Date as the basis and describes coverage through midnight of today's date.
- This is preliminary DC Index crime information. Historical records can change through classification changes, unfounded reports, or late reporting; the application's fine print does not guarantee timeliness or completeness. [Crime Cards](https://crimecards.dc.gov/), [official application text](https://crimecards.dc.gov/main.ff606deacb1bcd0e6575.js).

**Unknown:** No exact refresh hour, refresh timezone, completion SLA, or weekend/holiday exception was found in the current official help text or OCTO description. The published cutoff is not a promise that every prior-day report is available by a particular hour. The app's broad historical coverage description does not verify that a particular eight-year export is its maximum supported history.

## Annual Open Data DC Crime Incidents files

- The MPD-published description for [Crime Incidents in 2025](https://opendata.dc.gov/datasets/DCGIS::crime-incidents-in-2025/about), also preserved in the [government catalog's publisher metadata](https://catalog.data.gov/dataset/crime-incidents-in-2025), describes a subset of ASAP crime-report locations/attributes shared through an automated geocoding process. It does **not** state a refresh frequency, exact run time, or delivery lag. Annual naming identifies a year partition; it does not establish annual refresh frequency.
- The official [MPD feed service](https://maps2.dcgis.dc.gov/dcgis/rest/services/FEEDS/MPD/FeatureServer?f=pjson) lists separate year layers. Its [2025 layer metadata](https://maps2.dcgis.dc.gov/dcgis/rest/services/FEEDS/MPD/FeatureServer/7?f=pjson) declares date-field timezone `America/New_York`, respecting daylight saving time. That describes incident date fields, **not** the refresh scheduler's timezone. The layer response inspected did not expose `editingInfo.lastEditDate` or a documented refresh schedule.
- **Timestamp observation only:** the [MPD-published 2025 metadata in catalog.data.gov](https://catalog.data.gov/dataset/crime-incidents-in-2025) reports `modified: 2025-08-13T13:17:40.000Z` and `issued: 2025-01-06T17:02:34.000Z`. This is catalog/item metadata, potentially stale or describing metadata edits; it does not establish the newest incident, current CSV freshness, or cadence.
- The Crime Cards FAQ's OpenDataDC reference connects the products, but does not guarantee that each annual layer or generated CSV becomes current at the same instant as Crime Cards. The repository's [source notes](../../data/raw/sources.md) report that Crime Cards was fresher and that an eight-year export was used. That is project experience, not a current publisher SLA or independently verified comparison.

## Do not transfer other dashboard schedules

The [OGVP data page](https://www.buildingblocks.dc.gov/data) states a daily 7:40 AM refresh for its gun-violence dashboards, while the [Deputy Mayor's dashboard page](https://dmpsj.dc.gov/page/district-gun-violence-dashboards) says midnight. Both refer to **their dashboards**, separately linking to Crime Cards. Neither establishes a 7:40 AM or midnight refresh for Crime Cards or annual incident files; neither specifies a timezone in those statements.

## Scheduling recommendation

- **If consuming Crime Cards:** fetch once daily after the early-morning window, for example 10:00 AM `America/New_York`. The daily frequency follows the documented refresh; 10:00 AM and the scheduling timezone are project choices, not publisher guarantees. Permit reruns and preserve changes to historical records.
- **For the initial annual-file implementation:** a once-daily check is a reasonable conservative polling policy, but its frequency is not confirmed by annual-dataset documentation. Do not advertise next-day completeness. Record retrieval time, content hash, and maximum Report Date so repeated observations can establish actual freshness; recheck older partitions periodically for revisions. Increase or decrease polling based on measured changes or publisher confirmation, independently of Crime Cards' advertised cadence.

No implementation or schedule was changed during this research.

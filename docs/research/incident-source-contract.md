# Annual incident source contract

Researched 2026-11-15. Read-only endpoint research; no downloader implementation. Read alongside [cadence findings](crime-data-update-cadence.md) and [source notes](../../data/raw/sources.md).

## Discovery and downloads

The official [MPD FeatureServer inventory](https://maps2.dcgis.dc.gov/dcgis/rest/services/FEEDS/MPD/FeatureServer?f=pjson) exposes named annual layers. Observed mappings include 2024 → 6, 2025 → 7, and 2026 → 41, plus years back to 2008. IDs are not a formula based on year. Discover by exact annual layer name and validate the layer response; exclude “Last 30 Days.” New-year discovery can poll this inventory, but a publication date or January availability SLA is unknown. Absence of the current year must remain visible, while the previous-year refresh can proceed.

Official annual landing pages follow [Crime Incidents in 2025](https://opendata.dc.gov/datasets/DCGIS::crime-incidents-in-2025/about) and [Crime Incidents in 2026](https://opendata.dc.gov/datasets/DCGIS::crime-incidents-in-2026/about). These were application shells in this research tool. The 2026 item ID found in search is `c92a2cee0111473985c389e7a0805ea5`; its candidate CSV URL is `https://opendata.dc.gov/api/download/v1/items/c92a2cee0111473985c389e7a0805ea5/csv?layers=41`. **The CSV request and ArcGIS item JSON could not be read through this research tool.** Treat this as a candidate requiring a real download smoke test, not a verified transport contract. The annual feature layer itself is directly readable at `/FeatureServer/41?f=pjson`. A complete, verified item-ID/CSV manifest for historical years remains outstanding.

## Schema and identifiers

The [2025 layer](https://maps2.dcgis.dc.gov/dcgis/rest/services/FEEDS/MPD/FeatureServer/7?f=pjson) and [2026 layer](https://maps2.dcgis.dc.gov/dcgis/rest/services/FEEDS/MPD/FeatureServer/41?f=pjson) expose `CCN` (8-character Central Complaint Number), `REPORT_DAT`, `START_DATE`, `END_DATE`, `OFFENSE`, `METHOD`, `SHIFT`, geographic fields, `OBJECTID`, and nullable string `OCTO_RECORD_ID`. Preserve identifiers as strings. `OBJECTID` is the service's object ID; `CCN` has a nonunique index. Neither metadata response establishes that CCN is a unique row key or that OBJECTID/OCTO_RECORD_ID remains stable across publisher reloads. Full-year replacement avoids requiring such a promise; verify duplicate/null behavior before choosing a reconciliation key.

Both layers declare date-field timezone `America/New_York`, respecting DST. That describes source date semantics, not CSV formatting or scheduler timezone. Actual CSV headers, encoding, quoting, date representations, and historical schema consistency still require downloaded samples.

For a future REST fallback, these layers advertise pagination and ordering, a default `maxRecordCount` of 1,000, and JSON/GeoJSON/PBF query formats. The service-level limit is 2,000; use layer metadata instead. A single query is not a full-year export. Require explicit pagination, deterministic ordering, transfer-limit checks, and a count reconciliation; concurrent publisher updates can still affect a multipage snapshot.

## Change detection and freshness

Neither inspected annual layer exposes `editingInfo.lastEditDate`; `editFieldsInfo` is null. No reliable per-dataset data-edit watermark was established. Catalog/item modification time must not be treated as proof that incident rows changed, nor as proof that unchanged metadata means unchanged rows.

[Esri's download documentation](https://doc.esri.com/en/arcgis-hub/latest/build/data-download-settings.html) says Hub serves cached downloads when available and uses service last-edit information to determine whether a cache is outdated. Cache generation and search-index updates can take time. A freshly retrieved or regenerated CSV is therefore not a guarantee that its rows match the current live layer. [Hub's download metadata API](https://esri.github.io/hub.js/api/downloads/requestDownloadMetadata/) distinguishes optional `contentLastModified`, `lastEditDate`, `lastModified`, download status, and cache information; their actual availability and behavior for these DC items were not established.

No response-header/conditional-request experiment was completed: ETag, Last-Modified, HEAD support, redirect behavior, and 304 semantics for the final CSV object are **unknown**. Do not enable historical skipping based on those signals without verifying the exact endpoint. A representation validator only validates that representation; it does not establish upstream data freshness.

Design implication: daily full downloads of current/previous published years and a monthly full historical fallback are reasonable project policies. Metadata checks may trigger extra historical fetches, but cannot safely suppress the monthly fallback on the evidence above. Record retrieval time, source URL, content hash, row count, schema, and maximum report date. Missing or unreliable metadata is an explicit fallback condition, not “unchanged.” These policies are not publisher cadence guarantees.

"""DuckDB query helpers. All queries read directly from gzip CSVs — no separate DB needed."""

import duckdb

ARRESTS = "read_csv_auto('data/clean/arrest_data.csv.gz')"
INCIDENTS = "read_csv_auto('data/clean/incident_data_all.csv.gz')"
STOPS = "read_csv_auto('data/clean/stop_data.csv.gz')"
THREE11 = "read_csv_auto('data/clean/311_data_part_*.csv.gz')"

# 311 ward values are mixed strings ('1', '1.0') — normalize to integer
_311_WARD = "TRY_CAST(TRY_CAST(ward AS DOUBLE) AS INTEGER)"

WARDS = list(range(1, 9))
CURRENT_YEAR = 2024
PREV_YEAR = 2023


def _con() -> duckdb.DuckDBPyConnection:
    return duckdb.connect()


def _geo_filter(geo_type: str | None, geo_id: str | None) -> str:
    """Return a WHERE clause fragment for geographic filtering."""
    if not geo_type or not geo_id:
        return ""
    if geo_type == "ward":
        return f"AND ward = {int(geo_id)}"
    if geo_type == "anc":
        return f"AND anc_id = '{geo_id}'"
    if geo_type == "smd":
        return f"AND smd_id = '{geo_id}'"
    return ""


# ── Arrests ──────────────────────────────────────────────────────────────────

def arrests_by_year(geo_type=None, geo_id=None) -> list[dict]:
    geo = _geo_filter(geo_type, geo_id)
    rows = _con().execute(f"""
        SELECT year, COUNT(*) AS arrests
        FROM {ARRESTS}
        WHERE year BETWEEN 2015 AND {CURRENT_YEAR} {geo}
        GROUP BY year ORDER BY year
    """).fetchall()
    return [{"year": r[0], "arrests": r[1]} for r in rows]


def arrests_by_category(year=CURRENT_YEAR, geo_type=None, geo_id=None) -> list[dict]:
    geo = _geo_filter(geo_type, geo_id)
    rows = _con().execute(f"""
        SELECT category, COUNT(*) AS arrests
        FROM {ARRESTS}
        WHERE year = {year} AND category IS NOT NULL {geo}
        GROUP BY category ORDER BY arrests DESC
        LIMIT 15
    """).fetchall()
    return [{"category": r[0], "arrests": r[1]} for r in rows]


def arrests_yoy(geo_type=None, geo_id=None) -> list[dict]:
    """Year-over-year comparison by category for current vs prior year."""
    geo = _geo_filter(geo_type, geo_id)
    rows = _con().execute(f"""
        WITH base AS (
            SELECT category,
                COUNT(*) FILTER (WHERE year = {PREV_YEAR}) AS prev,
                COUNT(*) FILTER (WHERE year = {CURRENT_YEAR}) AS curr
            FROM {ARRESTS}
            WHERE year IN ({PREV_YEAR}, {CURRENT_YEAR})
              AND category IS NOT NULL {geo}
            GROUP BY category
        )
        SELECT category, prev, curr,
               curr - prev AS change,
               ROUND(100.0 * (curr - prev) / NULLIF(prev, 0), 1) AS pct_change
        FROM base
        WHERE prev > 0 OR curr > 0
        ORDER BY curr DESC
        LIMIT 20
    """).fetchall()
    return [
        {"category": r[0], "prev": r[1], "curr": r[2], "change": r[3], "pct_change": r[4]}
        for r in rows
    ]


def arrests_by_ward(year=CURRENT_YEAR) -> list[dict]:
    rows = _con().execute(f"""
        SELECT ward, COUNT(*) AS arrests
        FROM {ARRESTS}
        WHERE year = {year} AND ward IS NOT NULL
        GROUP BY ward ORDER BY ward
    """).fetchall()
    return [{"ward": r[0], "arrests": r[1]} for r in rows]


def available_ancs(geo_type=None, geo_id=None) -> list[str]:
    geo = _geo_filter(geo_type, geo_id)
    rows = _con().execute(f"""
        SELECT DISTINCT anc_id FROM {ARRESTS}
        WHERE anc_id IS NOT NULL {geo}
        ORDER BY anc_id
    """).fetchall()
    return [r[0] for r in rows]


def available_smds(anc_id: str) -> list[str]:
    rows = _con().execute(f"""
        SELECT DISTINCT smd_id FROM {ARRESTS}
        WHERE anc_id = '{anc_id}' AND smd_id IS NOT NULL
        ORDER BY smd_id
    """).fetchall()
    return [r[0] for r in rows]


# ── Incidents ─────────────────────────────────────────────────────────────────

def incidents_by_year(ward: int | None = None) -> list[dict]:
    geo = f"AND ward = {ward}" if ward else ""
    rows = _con().execute(f"""
        SELECT year, COUNT(*) AS incidents
        FROM {INCIDENTS}
        WHERE year BETWEEN 2016 AND {CURRENT_YEAR} {geo}
        GROUP BY year ORDER BY year
    """).fetchall()
    return [{"year": r[0], "incidents": r[1]} for r in rows]


def incidents_by_offense(year=CURRENT_YEAR, ward: int | None = None) -> list[dict]:
    geo = f"AND ward = {ward}" if ward else ""
    rows = _con().execute(f"""
        SELECT offense, COUNT(*) AS incidents
        FROM {INCIDENTS}
        WHERE year = {year} {geo}
        GROUP BY offense ORDER BY incidents DESC
        LIMIT 10
    """).fetchall()
    return [{"offense": r[0], "incidents": r[1]} for r in rows]


# ── 311 Service Requests ──────────────────────────────────────────────────────

def _311_ward_filter(ward: int | None) -> str:
    return f"AND {_311_WARD} = {ward}" if ward else ""


def requests_by_year(ward: int | None = None) -> list[dict]:
    geo = _311_ward_filter(ward)
    rows = _con().execute(f"""
        SELECT YEAR(ADDDATE) AS year, COUNT(*) AS requests
        FROM {THREE11}
        WHERE ADDDATE IS NOT NULL {geo}
        GROUP BY year ORDER BY year
    """).fetchall()
    return [{"year": r[0], "requests": r[1]} for r in rows]


def requests_by_service(year=CURRENT_YEAR, ward: int | None = None) -> list[dict]:
    geo = _311_ward_filter(ward)
    rows = _con().execute(f"""
        SELECT SERVICECODEDESCRIPTION AS service, COUNT(*) AS requests
        FROM {THREE11}
        WHERE YEAR(ADDDATE) = {year}
          AND SERVICECODEDESCRIPTION IS NOT NULL {geo}
        GROUP BY service ORDER BY requests DESC
        LIMIT 15
    """).fetchall()
    return [{"service": r[0], "requests": r[1]} for r in rows]


def requests_by_agency(year=CURRENT_YEAR, ward: int | None = None) -> list[dict]:
    geo = _311_ward_filter(ward)
    rows = _con().execute(f"""
        SELECT ORGANIZATIONACRONYM AS agency, COUNT(*) AS requests
        FROM {THREE11}
        WHERE YEAR(ADDDATE) = {year}
          AND ORGANIZATIONACRONYM IS NOT NULL {geo}
        GROUP BY agency ORDER BY requests DESC
        LIMIT 10
    """).fetchall()
    return [{"agency": r[0], "requests": r[1]} for r in rows]


def requests_by_ward(year=CURRENT_YEAR) -> list[dict]:
    rows = _con().execute(f"""
        SELECT {_311_WARD} AS ward, COUNT(*) AS requests
        FROM {THREE11}
        WHERE YEAR(ADDDATE) = {year}
          AND {_311_WARD} BETWEEN 1 AND 8
        GROUP BY ward ORDER BY ward
    """).fetchall()
    return [{"ward": r[0], "requests": r[1]} for r in rows]


def requests_yoy(ward: int | None = None) -> list[dict]:
    geo = _311_ward_filter(ward)
    rows = _con().execute(f"""
        WITH base AS (
            SELECT SERVICECODEDESCRIPTION AS service,
                COUNT(*) FILTER (WHERE YEAR(ADDDATE) = {PREV_YEAR}) AS prev,
                COUNT(*) FILTER (WHERE YEAR(ADDDATE) = {CURRENT_YEAR}) AS curr
            FROM {THREE11}
            WHERE YEAR(ADDDATE) IN ({PREV_YEAR}, {CURRENT_YEAR})
              AND SERVICECODEDESCRIPTION IS NOT NULL {geo}
            GROUP BY service
        )
        SELECT service, prev, curr,
               curr - prev AS change,
               ROUND(100.0 * (curr - prev) / NULLIF(prev, 0), 1) AS pct_change
        FROM base
        WHERE prev > 0 OR curr > 0
        ORDER BY curr DESC
        LIMIT 20
    """).fetchall()
    return [
        {"service": r[0], "prev": r[1], "curr": r[2], "change": r[3], "pct_change": r[4]}
        for r in rows
    ]


def requests_status_summary(year=CURRENT_YEAR, ward: int | None = None) -> list[dict]:
    """Normalize the messy status variants into Closed / Open / Other."""
    geo = _311_ward_filter(ward)
    rows = _con().execute(f"""
        SELECT
            CASE
                WHEN UPPER(SERVICEORDERSTATUS) LIKE 'CLOSED%' THEN 'Closed'
                WHEN UPPER(SERVICEORDERSTATUS) LIKE 'OPEN%'   THEN 'Open'
                WHEN UPPER(SERVICEORDERSTATUS) LIKE 'IN-PROG%'
                  OR UPPER(SERVICEORDERSTATUS) LIKE 'IN PROG%' THEN 'In Progress'
                WHEN UPPER(SERVICEORDERSTATUS) LIKE 'CANCEL%' THEN 'Canceled'
                ELSE 'Other'
            END AS status,
            COUNT(*) AS requests
        FROM {THREE11}
        WHERE YEAR(ADDDATE) = {year} {geo}
        GROUP BY status ORDER BY requests DESC
    """).fetchall()
    return [{"status": r[0], "requests": r[1]} for r in rows]


# ── Summary stats for front page ──────────────────────────────────────────────

def citywide_summary() -> dict:
    con = _con()
    arrests_curr = con.execute(f"SELECT COUNT(*) FROM {ARRESTS} WHERE year = {CURRENT_YEAR}").fetchone()[0]
    arrests_prev = con.execute(f"SELECT COUNT(*) FROM {ARRESTS} WHERE year = {PREV_YEAR}").fetchone()[0]
    incidents_curr = con.execute(f"SELECT COUNT(*) FROM {INCIDENTS} WHERE year = {CURRENT_YEAR}").fetchone()[0]
    incidents_prev = con.execute(f"SELECT COUNT(*) FROM {INCIDENTS} WHERE year = {PREV_YEAR}").fetchone()[0]
    req_curr = con.execute(f"SELECT COUNT(*) FROM {THREE11} WHERE YEAR(ADDDATE) = {CURRENT_YEAR}").fetchone()[0]
    req_prev = con.execute(f"SELECT COUNT(*) FROM {THREE11} WHERE YEAR(ADDDATE) = {PREV_YEAR}").fetchone()[0]

    def pct(curr, prev):
        return round(100 * (curr - prev) / prev, 1) if prev else 0

    return {
        "arrests_curr": arrests_curr,
        "arrests_prev": arrests_prev,
        "arrests_pct": pct(arrests_curr, arrests_prev),
        "incidents_curr": incidents_curr,
        "incidents_prev": incidents_prev,
        "incidents_pct": pct(incidents_curr, incidents_prev),
        "req_curr": req_curr,
        "req_prev": req_prev,
        "req_pct": pct(req_curr, req_prev),
        "current_year": CURRENT_YEAR,
        "prev_year": PREV_YEAR,
    }

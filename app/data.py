"""DuckDB query helpers. All queries read directly from gzip CSVs — no separate DB needed."""

import duckdb

ARRESTS = "read_csv_auto('data/clean/arrest_data.csv.gz')"
INCIDENTS = "read_csv_auto('data/clean/incident_data_all.csv.gz')"
STOPS = "read_csv_auto('data/clean/stop_data.csv.gz')"

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


# ── Summary stats for front page ──────────────────────────────────────────────

def citywide_summary() -> dict:
    con = _con()
    arrests_curr = con.execute(f"SELECT COUNT(*) FROM {ARRESTS} WHERE year = {CURRENT_YEAR}").fetchone()[0]
    arrests_prev = con.execute(f"SELECT COUNT(*) FROM {ARRESTS} WHERE year = {PREV_YEAR}").fetchone()[0]
    incidents_curr = con.execute(f"SELECT COUNT(*) FROM {INCIDENTS} WHERE year = {CURRENT_YEAR}").fetchone()[0]
    incidents_prev = con.execute(f"SELECT COUNT(*) FROM {INCIDENTS} WHERE year = {PREV_YEAR}").fetchone()[0]

    def pct(curr, prev):
        return round(100 * (curr - prev) / prev, 1) if prev else 0

    return {
        "arrests_curr": arrests_curr,
        "arrests_prev": arrests_prev,
        "arrests_pct": pct(arrests_curr, arrests_prev),
        "incidents_curr": incidents_curr,
        "incidents_prev": incidents_prev,
        "incidents_pct": pct(incidents_curr, incidents_prev),
        "current_year": CURRENT_YEAR,
        "prev_year": PREV_YEAR,
    }

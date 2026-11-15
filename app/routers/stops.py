from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app import data

router = APIRouter(prefix="/stops", tags=["stops"])
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def stops_index(
    request: Request,
    district: str | None = None,
    year: int = data.STOPS_CURRENT_YEAR,
):
    by_year = data.stops_by_year(district)
    by_district = data.stops_by_district(year)
    by_type = data.stops_by_type(year, district)
    by_ethnicity = data.stops_by_ethnicity(year, district)
    by_gender = data.stops_by_gender(year, district)
    search_summary = data.stops_search_summary(year, district)
    search_by_ethnicity = data.stops_search_by_ethnicity(year, district)

    geo_label = f"District {district}" if district else "Citywide"

    return templates.TemplateResponse("stops/index.html", {
        "request": request,
        "geo_label": geo_label,
        "district": district,
        "year": year,
        "by_year": by_year,
        "by_district": by_district,
        "by_type": by_type,
        "by_ethnicity": by_ethnicity,
        "by_gender": by_gender,
        "search_summary": search_summary,
        "search_by_ethnicity": search_by_ethnicity,
        "districts": data.DISTRICTS,
        "current_year": data.STOPS_CURRENT_YEAR,
    })

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app import data

router = APIRouter(prefix="/incidents", tags=["incidents"])
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def incidents_index(
    request: Request,
    ward: int | None = None,
    year: int = data.CURRENT_YEAR,
):
    by_year = data.incidents_by_year(ward)
    by_offense = data.incidents_by_offense(year, ward)

    geo_label = f"Ward {ward}" if ward else "Citywide"

    return templates.TemplateResponse("incidents/index.html", {
        "request": request,
        "geo_label": geo_label,
        "ward": ward,
        "year": year,
        "by_year": by_year,
        "by_offense": by_offense,
        "wards": data.WARDS,
        "current_year": data.CURRENT_YEAR,
        "prev_year": data.PREV_YEAR,
    })

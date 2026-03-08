from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app import data

router = APIRouter(prefix="/arrests", tags=["arrests"])
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def arrests_index(
    request: Request,
    geo_type: str | None = None,
    geo_id: str | None = None,
    year: int = data.CURRENT_YEAR,
):
    by_year = data.arrests_by_year(geo_type, geo_id)
    by_category = data.arrests_by_category(year, geo_type, geo_id)
    yoy = data.arrests_yoy(geo_type, geo_id)
    by_ward = data.arrests_by_ward(year)
    ancs = data.available_ancs()

    geo_label = f"{geo_type.upper()} {geo_id}" if geo_type and geo_id else "Citywide"

    return templates.TemplateResponse("arrests/index.html", {
        "request": request,
        "geo_label": geo_label,
        "geo_type": geo_type,
        "geo_id": geo_id,
        "year": year,
        "by_year": by_year,
        "by_category": by_category,
        "yoy": yoy,
        "by_ward": by_ward,
        "ancs": ancs,
        "wards": data.WARDS,
        "current_year": data.CURRENT_YEAR,
        "prev_year": data.PREV_YEAR,
    })

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app import data

router = APIRouter(prefix="/311", tags=["311"])
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def service_311_index(
    request: Request,
    ward: int | None = None,
    year: int = data.CURRENT_YEAR,
):
    by_year = data.requests_by_year(ward)
    by_service = data.requests_by_service(year, ward)
    by_agency = data.requests_by_agency(year, ward)
    by_ward = data.requests_by_ward(year)
    yoy = data.requests_yoy(ward)
    status = data.requests_status_summary(year, ward)

    geo_label = f"Ward {ward}" if ward else "Citywide"

    return templates.TemplateResponse("service_311/index.html", {
        "request": request,
        "geo_label": geo_label,
        "ward": ward,
        "year": year,
        "by_year": by_year,
        "by_service": by_service,
        "by_agency": by_agency,
        "by_ward": by_ward,
        "yoy": yoy,
        "status": status,
        "wards": data.WARDS,
        "current_year": data.CURRENT_YEAR,
        "prev_year": data.PREV_YEAR,
    })

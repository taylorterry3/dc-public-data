from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app import data
from app.routers import arrests, incidents, service_311

app = FastAPI(title="DC Public Data")
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(arrests.router)
app.include_router(incidents.router)
app.include_router(service_311.router)

templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    summary = data.citywide_summary()
    return templates.TemplateResponse("index.html", {"request": request, "summary": summary})

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/setup", response_class=HTMLResponse)
def setup(request: Request):
    return templates.TemplateResponse("setup.html", {"request": request})

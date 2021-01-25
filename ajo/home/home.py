from datetime import date

from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from .salary import Salary

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@router.post("/home", response_class=HTMLResponse)
async def home_form(
    request: Request,
    period: str = Form(...),
    salary: int = Form(...),
    start_date: date = Form(...),
    mojo: float = Form(...),
):

    saving_type = Salary(salary=salary)

    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "period": period,
            "salary": salary,
            "start_date": start_date,
            "mojo": mojo,
            "smile": salary * saving_type.smile,
            "maintenance": salary * saving_type.maintenance,
            "mojo_progress": saving_type.mojo_progress(mojo),
        },
    )

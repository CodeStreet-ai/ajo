from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from ajo.access import access
from ajo.home import home
from ajo.login import login

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


app.include_router(access.router)
app.include_router(home.router)
app.include_router(login.router)

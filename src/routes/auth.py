from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from src.config import Config

templates = Jinja2Templates(directory="src/templates")



router = APIRouter(
    prefix= "/auth",
    tags= ["auth"]
)

@router.get("/login")
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.get("/providers")
async def get_providers(request: Request):
    providers = Config.get("auth_providers")




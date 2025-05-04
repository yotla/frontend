from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="src/templates")

router = APIRouter(
    prefix= "/site",
    tags= ["site"]
)

@router.get("/")
async def root(request: Request):
   return templates.TemplateResponse("index.html", {"request": request})


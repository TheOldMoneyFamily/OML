from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/web", tags=["Home"])
templates = Jinja2Templates(directory="frontend/templates")

@router.get("/")
async def home(request: Request):
    \"\"\"
    Serves the homepage.
    \"\"\"
    return templates.TemplateResponse("index.html", {"request": request})

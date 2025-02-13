from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from dependencies import get_current_active_user

router = APIRouter(prefix="/web/dashboard", tags=["Dashboard"])
templates = Jinja2Templates(directory="frontend/templates")

@router.get("/")
async def dashboard(request: Request, user=Depends(get_current_active_user)):
    \"\"\"
    Serves the user dashboard.
    \"\"\"
    return templates.TemplateResponse("dashboard.html", {"request": request, "user": user})

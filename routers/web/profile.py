from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from dependencies import get_current_active_user

router = APIRouter(prefix="/web/profile", tags=["Profile"])
templates = Jinja2Templates(directory="frontend/templates")

@router.get("/")
async def profile(request: Request, user=Depends(get_current_active_user)):
    \"\"\"
    Serves the user profile page.
    \"\"\"
    return templates.TemplateResponse("profile.html", {"request": request, "user": user})

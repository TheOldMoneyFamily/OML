from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from services.auth_service import authenticate_user
from starlette.status import HTTP_302_FOUND

router = APIRouter(prefix="/web/login", tags=["Login"])
templates = Jinja2Templates(directory="frontend/templates")

@router.get("/")
async def login_page(request: Request):
    \"\"\"
    Serves the login page.
    \"\"\"
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/")
async def login(username: str = Form(...), password: str = Form(...)):
    \"\"\"
    Processes user login.
    \"\"\"
    user = authenticate_user(username, password)
    if user:
        return RedirectResponse(url="/web/dashboard", status_code=HTTP_302_FOUND)
    return RedirectResponse(url="/web/login", status_code=HTTP_302_FOUND)

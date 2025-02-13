from fastapi import APIRouter, Depends
from app.dependencies import get_current_user
from app.schemas import UserOut

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/home", response_model=UserOut)
def dashboard_home(current_user = Depends(get_current_user)):
    # Returns the current user's info as a simple dashboard home
    return current_user

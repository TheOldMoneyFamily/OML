from fastapi import APIRouter, Depends
from services.auth_service import authenticate_user, get_current_user

router = APIRouter(prefix="/api/auth", tags=["Authentication"])

@router.post("/login")
async def login(username: str, password: str):
    return authenticate_user(username, password)

@router.get("/profile")
async def profile(user=Depends(get_current_user)):
    return user

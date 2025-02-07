from fastapi import Depends, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
import redis
from config import settings
from services.auth_service import get_current_user
from database import SessionLocal

# OAuth2 authentication scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

# Initialize Redis connection
def get_redis():
    redis_client = redis.Redis.from_url(settings.REDIS_URL, decode_responses=True)
    try:
        yield redis_client
    finally:
        redis_client.close()

# Get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Dependency to get the current authenticated user
def get_current_active_user(token: str = Security(oauth2_scheme)):
    user = get_current_user(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid authentication")
    return user

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import schemas, crud, models
from app.dependencies import get_db, require_role

router = APIRouter(prefix="/admin", tags=["Admin"])
admin_required = require_role(models.UserRole.Admin)

@router.get("/users", response_model=List[schemas.UserOut])
def get_all_users(db: Session = Depends(get_db), user = Depends(admin_required)):
    users = db.query(models.User).all()
    return users

# Additional admin endpoints (user management, analytics, etc.) can be added here.

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud, models
from app.dependencies import get_db, require_role

router = APIRouter(prefix="/teacher", tags=["Teacher"])
teacher_required = require_role(models.UserRole.Teacher)

@router.post("/courses", response_model=schemas.CourseOut)
def add_course(course: schemas.CourseCreate, db: Session = Depends(get_db), user = Depends(teacher_required)):
    return crud.create_course(db, course)

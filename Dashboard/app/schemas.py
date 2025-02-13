from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date, datetime
import enum

class UserRole(str, enum.Enum):
    Admin = "Admin"
    User = "User"
    Subscriber = "Subscriber"
    Teacher = "Teacher"
    Student = "Student"
    Employee = "Employee"

class TaskStatus(str, enum.Enum):
    Pending = "Pending"
    InProgress = "In Progress"
    Completed = "Completed"

class UserBase(BaseModel):
    name: str
    email: EmailStr
    role: UserRole

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class CourseBase(BaseModel):
    title: str
    description: Optional[str] = None
    start_date: Optional[date]
    end_date: Optional[date]

class CourseCreate(CourseBase):
    teacher_id: int

class CourseOut(CourseBase):
    id: int
    teacher_id: int

    class Config:
        orm_mode = True

class SubscriptionBase(BaseModel):
    subscription_type: str
    start_date: Optional[date]
    end_date: Optional[date]

class SubscriptionCreate(SubscriptionBase):
    user_id: int

class SubscriptionOut(SubscriptionBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

class TaskBase(BaseModel):
    task_description: str
    due_date: Optional[date]
    status: Optional[TaskStatus] = TaskStatus.Pending

class TaskCreate(TaskBase):
    employee_id: int

class TaskOut(TaskBase):
    id: int
    employee_id: int

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

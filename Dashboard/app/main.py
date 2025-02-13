from fastapi import FastAPI
from app.routes import admin, dashboard, teacher, auth
from config import settings
from app.models import Base
from sqlalchemy import create_engine

# Create engine and initialize tables (for demo purposes; use Alembic for production migrations)
engine = create_engine(settings.DATABASE_URL)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Role-Based Dashboard API")

# Include authentication endpoints
app.include_router(auth.router, tags=["Auth"])
# Include role-specific endpoints
app.include_router(admin.router)
app.include_router(dashboard.router)
app.include_router(teacher.router)
# (Additional routers for User, Subscriber, Student, Employee can be added similarly)

@app.get("/")
def root():
    return {"message": "Welcome to the Role-Based Dashboard API"}

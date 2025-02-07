from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers.api import articles, fact_check, media, youtube, auth
from routers.web import home, dashboard, login, profile, upload
from config import settings

app = FastAPI(
    title="OML Writing Assistant API",
    description="GPT-powered assistant for structured article writing, fact-checking, and YouTube analytics.",
    version="2.0.0",
)

# API Routes
app.include_router(articles.router)
app.include_router(fact_check.router)
app.include_router(media.router)
app.include_router(youtube.router)
app.include_router(auth.router)

# UI Routes
app.include_router(home.router)
app.include_router(dashboard.router)
app.include_router(login.router)
app.include_router(profile.router)
app.include_router(upload.router)

# Serve Static Files (CSS, JS, Images)
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

@app.get("/")
def read_root():
    return {"message": "Welcome to OML Writing Assistant API"}

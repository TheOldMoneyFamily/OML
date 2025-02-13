from fastapi import APIRouter, Request, File, UploadFile, Depends
from fastapi.templating import Jinja2Templates
import shutil
import os

router = APIRouter(prefix="/web/upload", tags=["Upload"])
templates = Jinja2Templates(directory="frontend/templates")

UPLOAD_DIR = "uploads"

@router.get("/")
async def upload_page(request: Request):
    \"\"\"
    Serves the file upload page.
    \"\"\"
    return templates.TemplateResponse("upload.html", {"request": request})

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    \"\"\"
    Handles file uploads.
    \"\"\"
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    return {"filename": file.filename, "message": "Upload successful"}

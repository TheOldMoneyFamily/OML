import os
import shutil

STORAGE_DIR = "storage"

def save_file(file):
    \"\"\"
    Saves uploaded files.
    \"\"\"
    os.makedirs(STORAGE_DIR, exist_ok=True)
    file_path = os.path.join(STORAGE_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    return file_path

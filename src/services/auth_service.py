from fastapi import HTTPException
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def authenticate_user(username: str, password: str):
    \"\"\"
    Dummy authentication function.
    \"\"\"
    if username == "admin" and password == "password":
        return {"user": username, "message": "Login successful"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

def get_current_user():
    \"\"\"
    Mock function to retrieve an authenticated user.
    \"\"\"
    return {"username": "admin", "role": "editor"}

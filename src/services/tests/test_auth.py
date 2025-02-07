import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_login_success():
    \"\"\"
    Test successful login.
    \"\"\"
    response = client.post("/api/auth/login", data={
        "username": "admin",
        "password": "password"
    })
    assert response.status_code == 200
    assert response.json()["user"] == "admin"

def test_login_failure():
    \"\"\"
    Test login failure with incorrect credentials.
    \"\"\"
    response = client.post("/api/auth/login", data={
        "username": "wrong",
        "password": "wrong"
    })
    assert response.status_code == 401

import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_fact_check():
    \"\"\"
    Test the fact-checking API.
    \"\"\"
    response = client.post("/api/fact_check", json={
        "chapterContent": "The Rockefeller family is the richest in history."
    })
    assert response.status_code == 200
    assert "inaccuracies" in response.json()

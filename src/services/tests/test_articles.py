import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_write_article():
    \"\"\"
    Test article generation endpoint.
    \"\"\"
    response = client.post("/api/articles/write", json={
        "chapterNumber": 1,
        "subject": "Rockefeller Family",
        "wordCount": 495
    })
    assert response.status_code == 200
    assert "chapterContent" in response.json()

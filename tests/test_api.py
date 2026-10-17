from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_transcribe_endpoint():

    response = client.get("/docs")

    assert response.status_code == 200
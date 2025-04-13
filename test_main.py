from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_add_paper():
    response = client.post("/papers/", json={
        "id": 1,
        "title": "Sample Research",
        "author": "Obaid",
        "abstract": "This is a test abstract"
    })
    assert response.status_code == 200

def test_get_papers():
    response = client.get("/papers/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

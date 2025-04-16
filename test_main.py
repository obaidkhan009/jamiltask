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
    assert response.json() == {"message": "Paper added successfully"}


def test_add_duplicate_paper():
    response = client.post("/papers/", json={
        "id": 1,
        "title": "Duplicate Research",
        "author": "Obaid",
        "abstract": "Duplicate abstract"
    })
    assert response.status_code == 400
    assert response.json()["detail"] == "Paper ID already exists"


def test_get_papers():
    response = client.get("/papers/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) >= 1


def test_delete_existing_paper():
    response = client.delete("/papers/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Paper deleted successfully"}


def test_delete_nonexistent_paper():
    response = client.delete("/papers/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Paper not found"

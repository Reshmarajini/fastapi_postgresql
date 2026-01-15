from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"id": 105, "name": "Resma", "email": "reshmai@example.com"})
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 105
    assert data["name"] == "Resma"
    assert data["email"] == "reshmai@example.com"

def test_get_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

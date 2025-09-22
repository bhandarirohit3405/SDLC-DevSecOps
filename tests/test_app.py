import json
from app import app

def test_index():
    client = app.test_client()
    response = client.get("/")
    data = json.loads(response.data)
    assert response.status_code == 200
    assert "Welcome" in data["message"]

def test_greet():
    client = app.test_client()
    response = client.get("/greet?name=Atul")
    data = json.loads(response.data)
    assert "Hello, Atul" in data["greeting"]

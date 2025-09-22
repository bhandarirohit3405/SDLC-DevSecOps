import json
from app.app import app  # note: import from the package/module path

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
    assert response.status_code == 200
    assert data["greeting"].startswith("Hello, Atul")

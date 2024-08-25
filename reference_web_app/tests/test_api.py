from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_hello_world():
    response = client.get("/api/hello-world")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

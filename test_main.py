from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_and_list_tasks():
    response = client.post("/tasks", json={"title": "Buy milk"})
    assert response.status_code == 201
    task = response.json()
    assert task["title"] == "Buy milk"
    assert task["done"] is False
    assert task in client.get("/tasks").json()


def test_complete_task():
    task = client.post("/tasks", json={"title": "Call the bank"}).json()
    response = client.post(f"/tasks/{task['id']}/complete")
    assert response.status_code == 200
    assert response.json()["done"] is True


def test_delete_task():
    task = client.post("/tasks", json={"title": "Old idea"}).json()
    assert client.delete(f"/tasks/{task['id']}").status_code == 204
    assert task not in client.get("/tasks").json()


def test_missing_task_returns_404():
    assert client.post("/tasks/9999/complete").status_code == 404
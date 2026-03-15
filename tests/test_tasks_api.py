from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_healthcheck():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_and_get_task():
    payload = {
        "title": "First task",
        "description": "Write FastAPI project",
        "done": False,
    }

    # create
    create_resp = client.post("/tasks", json=payload)
    assert create_resp.status_code == 201
    created = create_resp.json()
    assert created["id"] == 1
    assert created["title"] == payload["title"]

    # get by id
    get_resp = client.get(f"/tasks/{created['id']}")
    assert get_resp.status_code == 200
    got = get_resp.json()
    assert got["id"] == created["id"]
    assert got["title"] == payload["title"]


def test_update_task():
    # create
    create_resp = client.post(
        "/tasks",
        json={"title": "To update", "description": "Old", "done": False},
    )
    task = create_resp.json()
    task_id = task["id"]

    # update
    update_payload = {"title": "Updated title", "done": True}
    update_resp = client.put(f"/tasks/{task_id}", json=update_payload)
    assert update_resp.status_code == 200
    updated = update_resp.json()
    assert updated["title"] == "Updated title"
    assert updated["done"] is True
    assert updated["description"] == "Old"


def test_delete_task():
    # create
    create_resp = client.post(
        "/tasks",
        json={"title": "To delete", "description": None, "done": False},
    )
    task_id = create_resp.json()["id"]

    # delete
    delete_resp = client.delete(f"/tasks/{task_id}")
    assert delete_resp.status_code == 204

    # return 404
    get_resp = client.get(f"/tasks/{task_id}")
    assert get_resp.status_code == 404

"""HTTP tests for task routes."""

from __future__ import annotations

from collections.abc import Iterator
from uuid import uuid4

import pytest
from fastapi.testclient import TestClient

from app.api.task_routes import get_task_service
from app.main import app
from app.repositories.task_repository import TaskRepository
from app.services.priority_advisor import Priority, PriorityAdvisor
from app.services.task_service import TaskService


class StubPriorityAdvisor(PriorityAdvisor):
    """Avoid external provider calls during route tests."""

    def suggest(self, title: str, description: str | None = None) -> Priority:
        """Return a deterministic priority suggestion."""
        return "medium"


@pytest.fixture
def client() -> Iterator[TestClient]:
    """Provide a client backed by a fresh in-memory repository."""
    service = TaskService(
        repository=TaskRepository(),
        priority_advisor=StubPriorityAdvisor(),
    )
    previous_override = app.dependency_overrides.get(get_task_service)
    app.dependency_overrides[get_task_service] = lambda: service

    try:
        with TestClient(app) as test_client:
            yield test_client
    finally:
        if previous_override is None:
            app.dependency_overrides.pop(get_task_service, None)
        else:
            app.dependency_overrides[get_task_service] = previous_override


def test_create_task_returns_201(client: TestClient) -> None:
    """Creates a task and returns the created representation."""
    response = client.post("/tasks", json={"title": "Write route tests"})

    assert response.status_code == 201
    assert response.json()["title"] == "Write route tests"


def test_read_and_update_task_return_200(client: TestClient) -> None:
    """Lists, reads, and updates tasks with successful status codes."""
    created = client.post("/tasks", json={"title": "Review API"}).json()
    task_id = created["id"]

    assert client.get("/tasks").status_code == 200
    assert client.get(f"/tasks/{task_id}").status_code == 200

    response = client.put(
        f"/tasks/{task_id}",
        json={"status": True},
    )

    assert response.status_code == 200
    assert response.json()["status"] is True


def test_delete_task_returns_204(client: TestClient) -> None:
    """Deletes an existing task without a response body."""
    created = client.post("/tasks", json={"title": "Remove old task"}).json()

    response = client.delete(f"/tasks/{created['id']}")

    assert response.status_code == 204
    assert response.content == b""


@pytest.mark.parametrize(
    ("method", "payload"),
    [
        ("GET", None),
        ("PUT", {"status": True}),
        ("DELETE", None),
    ],
)
def test_missing_task_returns_404(
    client: TestClient,
    method: str,
    payload: dict[str, bool] | None,
) -> None:
    """Returns 404 for operations targeting a missing task."""
    response = client.request(
        method,
        f"/tasks/{uuid4()}",
        json=payload,
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found."}
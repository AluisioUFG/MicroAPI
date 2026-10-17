"""Unit tests for task business rules."""

from __future__ import annotations

from uuid import uuid4

import pytest

from app.models.task import TaskCreate, TaskUpdate
from app.repositories.task_repository import TaskRepository
from app.services.priority_advisor import Priority, PriorityAdvisor
from app.services.task_service import TaskService


class StubPriorityAdvisor(PriorityAdvisor):
    """Deterministic priority advisor for tests."""

    def suggest(self, title: str, description: str | None = None) -> Priority:
        """Return a fixed priority suggestion."""
        return "medium"


@pytest.fixture
def task_repository() -> TaskRepository:
    """Provide an empty in-memory repository."""
    return TaskRepository()


@pytest.fixture
def task_service(task_repository: TaskRepository) -> TaskService:
    """Provide a task service with deterministic dependencies."""
    return TaskService(
        repository=task_repository,
        priority_advisor=StubPriorityAdvisor(),
    )


def test_create_task_stores_and_returns_task(task_service: TaskService) -> None:
    """Creates a task with generated metadata."""
    created_task = task_service.create(
        TaskCreate(title="Implement task routes", description="Expose CRUD endpoints."),
    )

    assert created_task.title == "Implement task routes"
    assert created_task.description == "Expose CRUD endpoints."
    assert created_task.status is False
    assert created_task.id is not None
    assert created_task.created_at.tzinfo is not None


def test_list_tasks_returns_all_created_tasks(task_service: TaskService) -> None:
    """Lists every task stored by the service."""
    first_task = task_service.create(TaskCreate(title="Create API routes"))
    second_task = task_service.create(TaskCreate(title="Write service tests"))

    tasks = task_service.list()

    assert [task.id for task in tasks] == [first_task.id, second_task.id]


def test_update_task_changes_provided_fields(task_service: TaskService) -> None:
    """Updates only fields supplied in the update payload."""
    created_task = task_service.create(
        TaskCreate(title="Implement repository", description="Initial version."),
    )

    updated_task = task_service.update(
        created_task.id,
        TaskUpdate(description="Completed implementation.", status=True),
    )

    assert updated_task is not None
    assert updated_task.title == "Implement repository"
    assert updated_task.description == "Completed implementation."
    assert updated_task.status is True


def test_delete_task_removes_existing_task(task_service: TaskService) -> None:
    """Deletes a task and makes it unavailable for retrieval."""
    created_task = task_service.create(TaskCreate(title="Remove temporary task"))

    was_deleted = task_service.delete(created_task.id)

    assert was_deleted is True
    assert task_service.get_by_id(created_task.id) is None


def test_missing_task_returns_safe_results(task_service: TaskService) -> None:
    """Returns safe values when a task identifier does not exist."""
    missing_task_id = uuid4()

    assert task_service.get_by_id(missing_task_id) is None
    assert task_service.update(missing_task_id, TaskUpdate(status=True)) is None
    assert task_service.delete(missing_task_id) is False

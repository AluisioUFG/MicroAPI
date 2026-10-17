"""Business rules for task management."""

from __future__ import annotations

from uuid import UUID

from app.models.task import TaskCreate, TaskOut, TaskUpdate
from app.repositories.task_repository import TaskRepository
from app.services.priority_advisor import Priority, PriorityAdvisor


class _PrioritySuggestionTracker:
    """Keeps priority suggestions synchronized with task changes."""

    def __init__(self, advisor: PriorityAdvisor) -> None:
        self._advisor = advisor
        self._suggestions: dict[UUID, Priority] = {}

    def refresh(self, task: TaskOut) -> None:
        self._suggestions[task.id] = self._advisor.suggest(
            task.title,
            task.description,
        )

    def remove(self, task_id: UUID) -> None:
        self._suggestions.pop(task_id, None)

    def get(self, task_id: UUID) -> Priority | None:
        return self._suggestions.get(task_id)


class TaskService:
    """Coordinates task persistence and priority suggestions."""

    def __init__(
        self,
        repository: TaskRepository,
        priority_advisor: PriorityAdvisor,
    ) -> None:
        """Initialize the service dependencies."""
        self._repository = repository
        self._priority_tracker = _PrioritySuggestionTracker(priority_advisor)

    def create(self, task: TaskCreate) -> TaskOut:
        """Create a task and calculate its priority suggestion."""
        created_task = self._repository.create(task)
        self._priority_tracker.refresh(created_task)
        return created_task

    def list(self) -> list[TaskOut]:
        """Return all tasks."""
        return self._repository.list()

    def get_by_id(self, task_id: UUID) -> TaskOut | None:
        """Return a task by identifier."""
        return self._repository.get_by_id(task_id)

    def update(self, task_id: UUID, task: TaskUpdate) -> TaskOut | None:
        """Update a task and refresh its priority suggestion."""
        updated_task = self._repository.update(task_id, task)
        if updated_task is None:
            return None

        self._priority_tracker.refresh(updated_task)
        return updated_task

    def delete(self, task_id: UUID) -> bool:
        """Delete a task and its associated suggestion."""
        was_deleted = self._repository.delete(task_id)
        if was_deleted:
            self._priority_tracker.remove(task_id)
        return was_deleted

    def get_suggested_priority(self, task_id: UUID) -> Priority | None:
        """Return the current priority suggestion for a task."""
        return self._priority_tracker.get(task_id)

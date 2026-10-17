"""In-memory repository for tasks."""

from __future__ import annotations

from datetime import datetime, timezone
from uuid import UUID, uuid4

from app.models.task import TaskCreate, TaskOut, TaskUpdate


class TaskRepository:
    """Stores tasks in memory for the initial release."""

    def __init__(self) -> None:
        self._tasks: dict[UUID, TaskOut] = {}

    def create(self, task: TaskCreate) -> TaskOut:
        """Create and store a task."""
        new_task = TaskOut(
            id=uuid4(),
            title=task.title,
            description=task.description,
            status=task.status,
            created_at=datetime.now(timezone.utc),
        )
        self._tasks[new_task.id] = new_task
        return new_task

    def list(self) -> list[TaskOut]:
        """Return all stored tasks."""
        return list(self._tasks.values())

    def get_by_id(self, task_id: UUID) -> TaskOut | None:
        """Return a task by identifier, when it exists."""
        return self._tasks.get(task_id)

    def update(self, task_id: UUID, task: TaskUpdate) -> TaskOut | None:
        """Apply provided fields to an existing task."""
        stored_task = self.get_by_id(task_id)
        if stored_task is None:
            return None

        updated_task = stored_task.model_copy(
            update=task.model_dump(exclude_unset=True),
        )
        self._tasks[task_id] = updated_task
        return updated_task

    def delete(self, task_id: UUID) -> bool:
        """Delete a task and report whether it existed."""
        return self._tasks.pop(task_id, None) is not None

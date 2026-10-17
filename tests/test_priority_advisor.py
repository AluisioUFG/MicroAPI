"""Tests for local priority suggestions and provider fallback."""

from __future__ import annotations

import pytest

from app.services.priority_advisor import Priority, PriorityAdvisor


@pytest.mark.parametrize(
    ("title", "description", "expected_priority"),
    [
        ("Resolve critical incident", None, "high"),
        ("Prepare weekly report", None, "medium"),
        ("Review backlog later", None, "low"),
    ],
)
def test_suggest_uses_local_priority_heuristic_without_api_key(
    monkeypatch: pytest.MonkeyPatch,
    title: str,
    description: str | None,
    expected_priority: Priority,
) -> None:
    """Classifies high, medium, and low priorities locally."""
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    advisor = PriorityAdvisor()

    assert advisor.suggest(title, description) == expected_priority


def test_suggest_falls_back_to_local_priority_when_provider_fails(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Keeps the local suggestion when the external provider raises."""
    monkeypatch.setenv("OPENAI_API_KEY", "test-api-key")
    advisor = PriorityAdvisor()

    def fail_provider(
        title: str,
        description: str | None,
        fallback: Priority,
    ) -> Priority:
        raise RuntimeError("provider unavailable")

    monkeypatch.setattr(advisor, "_suggest_with_llm", fail_provider)

    assert advisor.suggest("Urgent: restore service") == "high"
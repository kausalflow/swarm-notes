"""Base Skill protocol and abstract class for domain-specific paper analysis."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import ClassVar, Type

from pydantic import BaseModel


class PaperMetadata(BaseModel):
    """Generic metadata common to all paper types."""

    title: str
    authors: list[str]
    abstract: str
    tags: list[str]
    summary: str

    # Fields handled explicitly in the YAML frontmatter (not repeated in the
    # "extra fields" loop).
    _yaml_base_fields: ClassVar[frozenset[str]] = frozenset(
        {"title", "authors", "abstract", "tags", "summary"}
    )


class Skill(ABC):
    """Abstract base class for all domain Skills.

    Subclasses must define:
    - ``keywords``: A list of lowercase keyword strings used for lightweight triage.
    - ``system_prompt``: A domain-specific system prompt for the LLM analyst.
    - ``schema``: A Pydantic BaseModel subclass that defines the extraction schema.
    """

    keywords: ClassVar[list[str]]
    system_prompt: ClassVar[str]
    schema: ClassVar[Type[PaperMetadata]]

    @classmethod
    def matches(cls, title: str, abstract: str) -> bool:
        """Return True if any keyword appears in the title or abstract (case-insensitive)."""
        haystack = (title + " " + abstract).lower()
        return any(kw in haystack for kw in cls.keywords)

    @classmethod
    @abstractmethod
    def name(cls) -> str:
        """Human-readable name of the skill."""
        ...

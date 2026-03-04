"""
Language service layer.
Provides reusable query helpers consumed by views.
"""
from __future__ import annotations

from apps.languages.models import Language


def get_all_published_languages():
    """Return all published languages ordered by sort_order."""
    return Language.objects.filter(is_published=True).order_by("sort_order", "name")


def get_language_by_slug(slug: str) -> Language:
    """Return a single published language or raise Language.DoesNotExist."""
    return Language.objects.get(slug=slug, is_published=True)


def get_languages_with_quiz_counts():
    """
    Return published languages annotated with their published quiz count.
    Backend phase: annotate with Count('quiz_set') filtered by is_published=True.
    """
    return get_all_published_languages()

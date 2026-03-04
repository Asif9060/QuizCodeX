"""
Leaderboard service layer.
Handles ranking reads and entry upserts.
"""
from __future__ import annotations

from apps.leaderboard.models import LeaderboardEntry


def get_global_leaderboard(limit: int = 50):
    """Return global top-N leaderboard entries ordered by total_score."""
    return (
        LeaderboardEntry.objects
        .filter(language__isnull=True)
        .select_related("user")
        .order_by("rank")[:limit]
    )


def get_language_leaderboard(language_slug: str, limit: int = 50):
    """Return language-specific leaderboard entries ordered by rank."""
    return (
        LeaderboardEntry.objects
        .filter(language__slug=language_slug)
        .select_related("user", "language")
        .order_by("rank")[:limit]
    )


def upsert_leaderboard_entry(user, language=None) -> LeaderboardEntry:
    """
    Create or update a leaderboard entry after a quiz is completed.
    Backend phase: aggregate from UserResult, update rank for affected entries.
    """
    entry, _ = LeaderboardEntry.objects.get_or_create(
        user=user,
        language=language,
        defaults={"total_score": 0, "quizzes_completed": 0, "rank": 0},
    )
    return entry

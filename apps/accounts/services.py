"""
Accounts service layer.
Handles profile reads, score aggregation, and history queries.
"""
from __future__ import annotations

from django.contrib.auth import get_user_model

User = get_user_model()


def get_user_profile(username: str):
    """Return a user by username or raise User.DoesNotExist."""
    return User.objects.get(username=username)


def get_user_quiz_history(user, limit: int = 20):
    """
    Return the most recent UserResult records for a user.
    Backend phase: UserResult.objects.filter(user=user, is_completed=True)
                        .select_related('quiz__language').order_by('-completed_at')[:limit]
    """
    return []


def update_user_stats(user) -> None:
    """
    Recalculate and save total_score, quizzes_taken, best_streak from results.
    Called after a quiz is completed (connect to quiz_completed signal).
    """
    # Backend phase: aggregate from UserResult
    pass

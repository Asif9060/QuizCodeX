"""
Contests service layer — stub for future implementation.
Feature flag: FEATURE_FLAGS['CONTESTS'] must be True to expose contest routes.
"""
from __future__ import annotations


def get_active_contests():
    """
    Return currently active, published contests.
    Backend phase: Contest.objects.filter(is_published=True, is_active=True,
                        start_time__lte=now, end_time__gte=now)
    """
    return []


def register_participant(contest_id: int, user):
    """
    Register a user for a contest.
    Raises ValidationError if contest is full or registration closed.
    Backend phase: create ContestParticipant or raise.
    """
    raise NotImplementedError("Contests backend not yet implemented.")


def finalize_contest_rankings(contest_id: int) -> None:
    """
    Close a contest and assign final_rank to all participants.
    Backend phase: sort ContestParticipants by their UserResult score,
                   set final_rank, fire leaderboard update.
    """
    raise NotImplementedError("Contests backend not yet implemented.")

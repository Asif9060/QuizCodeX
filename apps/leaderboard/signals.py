"""
Leaderboard signal receivers.
Connected in LeaderboardConfig.ready().
"""
from django.dispatch import receiver
from apps.core.signals import quiz_completed


@receiver(quiz_completed)
def update_leaderboard(sender, user, quiz, **kwargs):
    """
    Upsert the user's LeaderboardEntry (global + language-specific) and
    reassign ranks for the affected scope.
    Fires after every completed quiz via quiz_completed signal.
    """
    from django.db.models import Sum, Count
    from apps.results.models import UserResult
    from apps.leaderboard.models import LeaderboardEntry

    language = quiz.language

    # Update for both global (language=None) and language-specific
    for lang in (None, language):
        filter_kwargs = {"user": user, "language": lang}
        qs = UserResult.objects.filter(user=user, is_completed=True)
        if lang:
            qs = qs.filter(quiz__language=lang)

        agg = qs.aggregate(
            total_score=Sum("score"),
            quizzes_completed=Count("id"),
        )

        entry, _ = LeaderboardEntry.objects.get_or_create(
            user=user, language=lang,
            defaults={"total_score": 0, "quizzes_completed": 0, "rank": 0},
        )
        entry.total_score = agg["total_score"] or 0
        entry.quizzes_completed = agg["quizzes_completed"] or 0
        entry.save(update_fields=["total_score", "quizzes_completed"])

    # Reassign ranks for the global leaderboard
    _reassign_ranks(language=None)
    _reassign_ranks(language=language)


def _reassign_ranks(language):
    """Re-number rank field for all entries in one leaderboard scope."""
    from apps.leaderboard.models import LeaderboardEntry
    entries = LeaderboardEntry.objects.filter(language=language).order_by("-total_score")
    for i, entry in enumerate(entries, start=1):
        if entry.rank != i:
            entry.rank = i
            entry.save(update_fields=["rank"])

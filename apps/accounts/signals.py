"""
Accounts signal receivers.
Connected in AccountsConfig.ready() — keep imports inside the function
to avoid circular imports at module load time.
"""
from django.dispatch import receiver
from apps.core.signals import quiz_completed


@receiver(quiz_completed)
def update_user_stats(sender, user, quiz, **kwargs):
    """
    Recalculate CustomUser aggregate fields after every completed quiz.
    Called automatically when results.services.complete_quiz() fires quiz_completed.
    """
    from django.db.models import Sum, Count
    from apps.results.models import UserResult

    completed = UserResult.objects.filter(user=user, is_completed=True)

    agg = completed.aggregate(
        total_score=Sum("score"),
        quizzes_taken=Count("id"),
    )

    # Best streak: consecutive days with at least one completed quiz
    # Simple version: count unique days — full streak logic can be added later
    user.total_score = agg["total_score"] or 0
    user.quizzes_taken = agg["quizzes_taken"] or 0
    user.save(update_fields=["total_score", "quizzes_taken"])

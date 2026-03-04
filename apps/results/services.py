"""
Results service layer.
"""
from django.db import transaction
from apps.results.models import UserResult, UserAnswer


def create_quiz_attempt(user, quiz):
    """Start a new quiz attempt and return the UserResult."""
    return UserResult.objects.create(
        user=user,
        quiz=quiz,
        total_points=sum(q.points for q in quiz.questions.all()),
    )


def submit_answer(result: UserResult, question, selected_option):
    """Record a user's answer for a question. Returns (UserAnswer, is_correct)."""
    answer, _ = UserAnswer.objects.get_or_create(
        result=result,
        question=question,
        defaults={"selected_option": selected_option},
    )
    return answer, answer.is_correct


@transaction.atomic
def complete_quiz(result: UserResult):
    """Finalize a quiz attempt: calculate score, mark complete."""
    from django.utils import timezone
    from apps.core.signals import quiz_completed

    correct_answers = result.answers.filter(selected_option__is_correct=True)
    result.score = sum(a.question.points for a in correct_answers)
    result.is_completed = True
    result.completed_at = timezone.now()
    result.save(update_fields=["score", "is_completed", "completed_at"])

    # Fire decoupled signal — leaderboard, contests, AI hook in here
    quiz_completed.send(sender=result, user=result.user, quiz=result.quiz)

    return result

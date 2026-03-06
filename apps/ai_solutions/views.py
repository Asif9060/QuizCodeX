"""AI Solutions views -- staff-only AJAX endpoints."""
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

from apps.quizzes.models import Question


@require_POST
@staff_member_required
def generate_explanation_view(request, question_id: int):
    """
    AJAX endpoint: POST /ai/generate/<question_id>/
    Generates an AI explanation for the given question and returns it as JSON.
    Only accessible to staff members.
    """
    question = get_object_or_404(Question, pk=question_id)

    if not question.options.exists():
        return JsonResponse(
            {"ok": False, "error": "This question has no options yet. Add options before generating an explanation."},
            status=400,
        )

    if not question.options.filter(is_correct=True).exists():
        return JsonResponse(
            {"ok": False, "error": "No correct option is marked. Mark one option as correct first."},
            status=400,
        )

    try:
        from apps.ai_solutions.services import generate_explanation
        text = generate_explanation(question)
        return JsonResponse({"ok": True, "explanation": text})
    except Exception as exc:
        return JsonResponse({"ok": False, "error": str(exc)}, status=500)


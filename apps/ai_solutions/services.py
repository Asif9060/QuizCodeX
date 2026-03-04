"""
AI Solutions service layer — stub for future implementation.
Feature flag: FEATURE_FLAGS['AI_EXPLANATIONS'] must be True to expose AI routes.
"""
from __future__ import annotations


def get_explanation_for_question(question_id: int):
    """
    Return the approved AIExplanation for a question, or None.
    Backend phase: AIExplanation.objects.filter(question_id=question_id, is_approved=True).first()
    """
    return None


def generate_explanation(question_id: int) -> None:
    """
    Call the configured LLM API, save AIExplanation, and mark is_approved=False
    (pending admin review).
    Backend phase:
        - Build prompt from Question.text + correct Option.text
        - Call OpenAI / Gemini API
        - AIExplanation.objects.update_or_create(question_id=question_id, ...)
    """
    raise NotImplementedError("AI backend not yet implemented.")


def approve_explanation(explanation_id: int) -> None:
    """
    Mark an AIExplanation as approved (called from admin action or view).
    Backend phase: AIExplanation.objects.filter(pk=explanation_id).update(is_approved=True)
    """
    raise NotImplementedError("AI backend not yet implemented.")

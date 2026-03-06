"""AI Solutions service layer.

Public API:
  generate_explanation(question)  -- generate + save + return explanation text
  get_explanation_for_question(question_id)  -- fetch approved explanation or None
  approve_explanation(explanation_id)  -- mark approved
"""
from __future__ import annotations


def build_explanation_prompt(question) -> str:
    """Build the LLM prompt from a Question instance and its Options."""
    options_block = ""
    for opt in question.options.order_by("order"):
        marker = "\u2713" if opt.is_correct else "\u2022"
        options_block += f"  {marker} {opt.text}\n"

    return (
        "You are an expert programming instructor. "
        "Write a clear, concise explanation (3-5 sentences) for why the correct answer to "
        "the following multiple-choice question is correct. "
        "Also briefly explain why the other options are incorrect. "
        "Use plain language suitable for a developer learning the topic.\n\n"
        f"Question:\n{question.text}\n\n"
        f"Options (\u2713 = correct):\n{options_block}\n"
        "Explanation:"
    )


def generate_explanation(question) -> str:
    """
    Call the active AI provider, save/update an AIExplanation record,
    sync the text back to question.explanation, and return the generated text.
    """
    from apps.ai_solutions.models import AIExplanation
    from apps.ai_solutions.providers import get_active_provider
    from django.conf import settings

    provider = get_active_provider()
    prompt = build_explanation_prompt(question)
    text, prompt_tokens, completion_tokens = provider.generate(prompt)

    model_name = settings.AI_PROVIDERS.get(settings.AI_ACTIVE_PROVIDER, {}).get(
        "model", settings.AI_ACTIVE_PROVIDER
    )

    AIExplanation.objects.update_or_create(
        question=question,
        defaults={
            "content": text,
            "model_used": model_name,
            "prompt_tokens": prompt_tokens,
            "completion_tokens": completion_tokens,
            "is_approved": True,
        },
    )

    # Sync into the question's own explanation field so it shows on the quiz
    question.explanation = text
    question.save(update_fields=["explanation"])

    return text


def get_explanation_for_question(question_id: int):
    """Return the approved AIExplanation for a question, or None."""
    from apps.ai_solutions.models import AIExplanation
    return AIExplanation.objects.filter(
        question_id=question_id, is_approved=True
    ).first()


def approve_explanation(explanation_id: int) -> None:
    """Mark an AIExplanation as approved."""
    from apps.ai_solutions.models import AIExplanation
    AIExplanation.objects.filter(pk=explanation_id).update(is_approved=True)

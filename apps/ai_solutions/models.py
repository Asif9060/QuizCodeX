"""
AI Solutions app models — LLM-generated explanations for quiz questions.
Feature flag: AI_EXPLANATIONS_ENABLED
Future: populated via Celery tasks calling OpenAI / Gemini API.
"""
from django.db import models
from apps.core.models import TimeStampedModel


class AIExplanation(TimeStampedModel):
    question = models.OneToOneField("quizzes.Question", on_delete=models.CASCADE, related_name="ai_explanation")
    content = models.TextField()
    model_used = models.CharField(max_length=100, blank=True, help_text="e.g. gpt-4o, gemini-1.5-pro")
    prompt_tokens = models.PositiveIntegerField(default=0)
    completion_tokens = models.PositiveIntegerField(default=0)
    is_approved = models.BooleanField(default=False, help_text="Admin must approve before showing to users")

    class Meta:
        verbose_name = "AI Explanation"
        verbose_name_plural = "AI Explanations"

    def __str__(self):
        return f"AI Explanation for Q{self.question_id}"

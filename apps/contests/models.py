"""
Contests app models — timed competitive quiz sessions.
Feature flag: CONTESTS_ENABLED
Future: uses Celery + Redis for real-time timers.
"""
from django.db import models
from django.conf import settings
from apps.core.models import PublishableModel


class Contest(PublishableModel):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    quiz = models.ForeignKey("quizzes.Quiz", on_delete=models.CASCADE, related_name="contests")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    max_participants = models.PositiveIntegerField(null=True, blank=True, help_text="Leave blank for unlimited")
    is_active = models.BooleanField(default=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ["-start_time"]
        verbose_name = "Contest"
        verbose_name_plural = "Contests"

    def __str__(self):
        return self.title


class ContestParticipant(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE, related_name="participants")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    result = models.OneToOneField("results.UserResult", null=True, blank=True, on_delete=models.SET_NULL)
    joined_at = models.DateTimeField(auto_now_add=True)
    final_rank = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        unique_together = [("contest", "user")]
        verbose_name = "Contest Participant"
        verbose_name_plural = "Contest Participants"

    def __str__(self):
        return f"{self.user} in {self.contest}"

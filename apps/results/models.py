"""
Results app models — UserResult and UserAnswer (attempt tracking).
"""
from django.db import models
from django.conf import settings
from apps.core.models import TimeStampedModel


class UserResult(TimeStampedModel):
    """One record per quiz attempt."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="results")
    quiz = models.ForeignKey("quizzes.Quiz", on_delete=models.CASCADE, related_name="results")
    score = models.PositiveIntegerField(default=0)
    total_points = models.PositiveIntegerField(default=0)
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    class Meta:
        ordering = ["-started_at"]
        verbose_name = "User Result"
        verbose_name_plural = "User Results"

    def __str__(self):
        return f"{self.user} — {self.quiz} ({self.score}/{self.total_points})"

    @property
    def percentage(self):
        if self.total_points == 0:
            return 0
        return round((self.score / self.total_points) * 100)

    @property
    def time_taken(self):
        """Human-readable duration, e.g. '4m 38s'."""
        if not self.completed_at or not self.started_at:
            return None
        delta = self.completed_at - self.started_at
        total_seconds = int(delta.total_seconds())
        minutes, seconds = divmod(total_seconds, 60)
        if minutes:
            return f"{minutes}m {seconds}s"
        return f"{seconds}s"

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("results:detail", kwargs={"pk": self.pk})


class UserAnswer(TimeStampedModel):
    """One record per question answered in an attempt."""
    result = models.ForeignKey(UserResult, on_delete=models.CASCADE, related_name="answers")
    question = models.ForeignKey("quizzes.Question", on_delete=models.CASCADE)
    selected_option = models.ForeignKey("quizzes.Option", null=True, blank=True, on_delete=models.SET_NULL)
    answered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "User Answer"
        verbose_name_plural = "User Answers"
        unique_together = [("result", "question")]

    def __str__(self):
        return f"{self.result.user} — {self.question}"

    @property
    def is_correct(self):
        return self.selected_option is not None and self.selected_option.is_correct

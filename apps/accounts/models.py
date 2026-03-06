"""
Accounts app models — custom User with profile fields.
Always use AbstractUser from day one; swapping the user model after migration is painful.
"""
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    bio = models.TextField(max_length=300, blank=True)
    total_score = models.PositiveIntegerField(default=0)
    quizzes_taken = models.PositiveIntegerField(default=0)
    best_streak = models.PositiveIntegerField(default=0)

    # Social login (future: django-allauth)
    # provider = models.CharField(max_length=30, blank=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["-date_joined"]

    def __str__(self):
        return self.username

    @property
    def display_name(self):
        return self.get_full_name() or self.username

    @property
    def favorite_language(self):
        """Derive the most-used language from completed quiz results."""
        from django.db.models import Count
        entry = (
            self.results
            .filter(is_completed=True)
            .values("quiz__language__name")
            .annotate(cnt=Count("id"))
            .order_by("-cnt")
            .first()
        )
        return entry["quiz__language__name"] if entry else None

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("accounts:profile", kwargs={"username": self.username})

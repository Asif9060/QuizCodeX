"""
Core app — abstract base models shared across all domain apps.
"""
from django.db import models
from django.utils import timezone


class TimeStampedModel(models.Model):
    """Abstract base: created_at / updated_at timestamps."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PublishableModel(TimeStampedModel):
    """Abstract base: publish/unpublish workflow."""
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def publish(self):
        self.is_published = True
        self.published_at = timezone.now()
        self.save(update_fields=["is_published", "published_at"])

    def unpublish(self):
        self.is_published = False
        self.published_at = None
        self.save(update_fields=["is_published", "published_at"])

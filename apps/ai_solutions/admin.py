from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import AIExplanation


@admin.register(AIExplanation)
class AIExplanationAdmin(ModelAdmin):
    list_display = ("question", "model_used", "is_approved", "prompt_tokens", "completion_tokens", "created_at")
    list_filter = ("is_approved", "model_used")
    search_fields = ("question__text", "content")
    list_editable = ("is_approved",)
    readonly_fields = ("created_at", "updated_at", "prompt_tokens", "completion_tokens")

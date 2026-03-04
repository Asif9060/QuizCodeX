from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Language


@admin.register(Language)
class LanguageAdmin(ModelAdmin):
    list_display = ("name", "slug", "sort_order", "is_published", "published_quiz_count", "created_at")
    list_filter = ("is_published",)
    search_fields = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}
    list_editable = ("sort_order", "is_published")
    ordering = ("sort_order", "name")
    readonly_fields = ("created_at", "updated_at")

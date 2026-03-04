from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Contest, ContestParticipant


@admin.register(Contest)
class ContestAdmin(ModelAdmin):
    list_display = ("title", "quiz", "start_time", "end_time", "is_active", "is_published")
    list_filter = ("is_active", "is_published")
    search_fields = ("title",)


@admin.register(ContestParticipant)
class ContestParticipantAdmin(ModelAdmin):
    list_display = ("user", "contest", "final_rank", "joined_at")
    list_filter = ("contest",)
    search_fields = ("user__username",)

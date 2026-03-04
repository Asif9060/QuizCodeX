from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from .models import Quiz, Question, Option


class OptionInline(TabularInline):
    model = Option
    extra = 4
    fields = ("text", "is_correct", "order")


class QuestionInline(TabularInline):
    model = Question
    extra = 1
    show_change_link = True
    fields = ("text", "question_type", "points", "order")


@admin.register(Quiz)
class QuizAdmin(ModelAdmin):
    list_display = ("title", "language", "difficulty", "question_count", "time_limit", "is_published", "created_at")
    list_filter = ("is_published", "difficulty", "language")
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ("is_published",)
    inlines = [QuestionInline]
    readonly_fields = ("created_at", "updated_at")
    autocomplete_fields = ["language"]


@admin.register(Question)
class QuestionAdmin(ModelAdmin):
    list_display = ("__str__", "quiz", "question_type", "points", "order")
    list_filter = ("question_type", "quiz__language")
    search_fields = ("text",)
    inlines = [OptionInline]
    autocomplete_fields = ["quiz"]

"""Core views — home page."""
from django.shortcuts import render
from django.db.models import Count, Q
from django.contrib.auth import get_user_model

from apps.languages.models import Language
from apps.quizzes.models import Quiz
from apps.results.models import UserResult

User = get_user_model()


def home(request):
    languages = (
        Language.objects
        .filter(is_published=True)
        .annotate(quiz_count=Count("quiz", filter=Q(quiz__is_published=True)))
        .order_by("sort_order", "name")
    )

    lang_list = list(languages)
    stats = {
        "total_languages": len(lang_list),
        "total_quizzes": Quiz.objects.filter(is_published=True).count(),
        "total_users": User.objects.count(),
        "quizzes_taken": UserResult.objects.filter(is_completed=True).count(),
    }

    return render(request, "home.html", {
        "featured_languages": lang_list[:6],
        "all_languages": lang_list,
        "stats": stats,
    })

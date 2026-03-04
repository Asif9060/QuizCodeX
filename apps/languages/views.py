"""Languages views — language catalog and detail."""
from django.shortcuts import render
from apps.core.views import SAMPLE_LANGUAGES


def language_list(request):
    return render(request, "languages/list.html", {
        "languages": SAMPLE_LANGUAGES,
    })


def language_detail(request, slug):
    lang = next((l for l in SAMPLE_LANGUAGES if l["slug"] == slug), SAMPLE_LANGUAGES[0])
    sample_quizzes = [
        {"title": "Python Basics", "slug": "python-basics", "difficulty": "Beginner", "question_count": 10, "time_limit": 600},
        {"title": "Python OOP", "slug": "python-oop", "difficulty": "Intermediate", "question_count": 15, "time_limit": 900},
        {"title": "Python Data Structures", "slug": "python-data-structures", "difficulty": "Intermediate", "question_count": 20, "time_limit": 1200},
        {"title": "Python Advanced", "slug": "python-advanced", "difficulty": "Advanced", "question_count": 25, "time_limit": 1800},
        {"title": "Python Decorators", "slug": "python-decorators", "difficulty": "Advanced", "question_count": 10, "time_limit": 900},
    ]
    return render(request, "quizzes/list.html", {
        "language": lang,
        "quizzes": sample_quizzes,
    })

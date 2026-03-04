"""Accounts views — login, register, profile."""
from django.shortcuts import render
from apps.results.views import SAMPLE_REVIEW

SAMPLE_HISTORY = [
    {"quiz": "Python Basics", "quiz_slug": "python-basics", "language": "Python", "score": 80, "total": 100, "date": "2026-03-01", "result_id": 1},
    {"quiz": "JavaScript ES6", "quiz_slug": "javascript-es6", "language": "JavaScript", "score": 70, "total": 100, "date": "2026-02-28", "result_id": 2},
    {"quiz": "Python OOP", "quiz_slug": "python-oop", "language": "Python", "score": 90, "total": 100, "date": "2026-02-25", "result_id": 3},
    {"quiz": "Java Collections", "quiz_slug": "java-collections", "language": "Java", "score": 60, "total": 100, "date": "2026-02-20", "result_id": 4},
]


def login_view(request):
    return render(request, "accounts/login.html", {})


def register_view(request):
    return render(request, "accounts/register.html", {})


def profile_view(request, username="demo_user"):
    return render(request, "accounts/profile.html", {
        "profile_user": {
            "username": username,
            "display_name": "Demo User",
            "bio": "Passionate about clean code and algorithms.",
            "total_score": 3840,
            "quizzes_taken": 48,
            "best_streak": 12,
            "date_joined": "January 2026",
            "favorite_language": "Python",
        },
        "history": SAMPLE_HISTORY,
        "stats": {
            "avg_score": 75,
            "languages_tried": 5,
            "total_correct": 192,
        }
    })

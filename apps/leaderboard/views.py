"""Leaderboard views — global and per-language rankings."""
from django.shortcuts import render
from apps.core.views import SAMPLE_LANGUAGES

SAMPLE_LEADERS = [
    {"rank": 1, "username": "ByteMaster99", "total_score": 4850, "quizzes": 97, "badge": "gold"},
    {"rank": 2, "username": "CodeNinja_X", "total_score": 4620, "quizzes": 92, "badge": "gold"},
    {"rank": 3, "username": "AlgoQueen", "total_score": 4330, "quizzes": 87, "badge": "gold"},
    {"rank": 4, "username": "DevHero2026", "total_score": 4100, "quizzes": 82, "badge": "silver"},
    {"rank": 5, "username": "StackSlayer", "total_score": 3980, "quizzes": 80, "badge": "silver"},
    {"rank": 6, "username": "RuntimeKing", "total_score": 3750, "quizzes": 75, "badge": "silver"},
    {"rank": 7, "username": "NullPointer7", "total_score": 3400, "quizzes": 68, "badge": "bronze"},
    {"rank": 8, "username": "PythonWizard", "total_score": 3200, "quizzes": 64, "badge": "bronze"},
    {"rank": 9, "username": "JSEnjoyer", "total_score": 2990, "quizzes": 60, "badge": "bronze"},
    {"rank": 10, "username": "SyntaxSage", "total_score": 2800, "quizzes": 56, "badge": None},
]


def leaderboard_index(request):
    return render(request, "leaderboard/index.html", {
        "leaders": SAMPLE_LEADERS,
        "podium": SAMPLE_LEADERS[:3],
        "rest": SAMPLE_LEADERS[3:],
        "languages": SAMPLE_LANGUAGES,
        "active_tab": "all",
    })

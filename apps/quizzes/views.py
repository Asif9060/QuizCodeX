"""Quizzes views — quiz-taking experience."""
from django.shortcuts import render

SAMPLE_QUESTIONS = [
    {
        "id": 1, "text": "What is the output of print(type([])) in Python?",
        "options": [
            {"id": 1, "text": "<class 'list'>"},
            {"id": 2, "text": "<class 'tuple'>"},
            {"id": 3, "text": "<class 'dict'>"},
            {"id": 4, "text": "<class 'set'>"},
        ]
    },
    {
        "id": 2, "text": "Which keyword is used to define a function in Python?",
        "options": [
            {"id": 1, "text": "function"},
            {"id": 2, "text": "def"},
            {"id": 3, "text": "func"},
            {"id": 4, "text": "define"},
        ]
    },
    {
        "id": 3, "text": "What does PEP stand for?",
        "options": [
            {"id": 1, "text": "Python Enhancement Proposal"},
            {"id": 2, "text": "Python Execution Protocol"},
            {"id": 3, "text": "Python Editor Plugin"},
            {"id": 4, "text": "Programmatic Extension Package"},
        ]
    },
]


def quiz_take(request, slug):
    return render(request, "quizzes/take.html", {
        "quiz": {"title": "Python Basics", "slug": slug, "time_limit": 600, "question_count": len(SAMPLE_QUESTIONS)},
        "questions": SAMPLE_QUESTIONS,
        "total_questions": len(SAMPLE_QUESTIONS),
        "language": {"name": "Python", "slug": "python", "icon_char": "Py", "color": "#3776AB"},
        "results_url": "/results/1/",
    })

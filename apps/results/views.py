"""Results views — score and review screens."""
from django.shortcuts import render

SAMPLE_REVIEW = [
    {
        "number": 1,
        "text": "What is the output of print(type([])) in Python?",
        "your_answer": "<class 'list'>",
        "correct_answer": "<class 'list'>",
        "is_correct": True,
        "explanation": "The list() constructor creates a list object. type([]) returns <class 'list'>.",
    },
    {
        "number": 2,
        "text": "Which keyword is used to define a function in Python?",
        "your_answer": "function",
        "correct_answer": "def",
        "is_correct": False,
        "explanation": "In Python, functions are defined using the 'def' keyword, not 'function' as in JavaScript.",
    },
    {
        "number": 3,
        "text": "What does PEP stand for?",
        "your_answer": "Python Enhancement Proposal",
        "correct_answer": "Python Enhancement Proposal",
        "is_correct": True,
        "explanation": "PEP stands for Python Enhancement Proposal. PEPs describe new features, processes, or environments for Python.",
    },
]


def result_detail(request, pk=1):
    correct = sum(1 for q in SAMPLE_REVIEW if q["is_correct"])
    total = len(SAMPLE_REVIEW)
    return render(request, "results/detail.html", {
        "result": {
            "id": pk,
            "score": correct * 10,
            "total_points": total * 10,
            "percentage": round((correct / total) * 100),
            "correct": correct,
            "incorrect": total - correct,
            "skipped": 0,
            "time_taken": "4m 38s",
            "quiz": {"title": "Python Basics", "slug": "python-basics"},
            "language": {"name": "Python", "slug": "python", "icon_char": "Py"},
        },
        "review": SAMPLE_REVIEW,
    })

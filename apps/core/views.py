"""Core views — home page."""
from django.shortcuts import render

# ─── Static placeholder data — replaced by real DB queries in backend phase ───
SAMPLE_LANGUAGES = [
    {"name": "Python", "slug": "python", "quiz_count": 50, "difficulty": "Beginner", "icon_char": "Py", "color": "#3776AB"},
    {"name": "JavaScript", "slug": "javascript", "quiz_count": 50, "difficulty": "Beginner", "icon_char": "JS", "color": "#F7DF1E"},
    {"name": "Java", "slug": "java", "quiz_count": 50, "difficulty": "Intermediate", "icon_char": "Jv", "color": "#ED8B00"},
    {"name": "C++", "slug": "cpp", "quiz_count": 50, "difficulty": "Advanced", "icon_char": "C+", "color": "#00599C"},
    {"name": "TypeScript", "slug": "typescript", "quiz_count": 50, "difficulty": "Intermediate", "icon_char": "TS", "color": "#3178C6"},
    {"name": "Go", "slug": "go", "quiz_count": 50, "difficulty": "Intermediate", "icon_char": "Go", "color": "#00ADD8"},
    {"name": "Rust", "slug": "rust", "quiz_count": 50, "difficulty": "Advanced", "icon_char": "Rs", "color": "#CE412B"},
    {"name": "PHP", "slug": "php", "quiz_count": 50, "difficulty": "Beginner", "icon_char": "Ph", "color": "#777BB4"},
    {"name": "Ruby", "slug": "ruby", "quiz_count": 50, "difficulty": "Beginner", "icon_char": "Rb", "color": "#CC342D"},
    {"name": "Swift", "slug": "swift", "quiz_count": 50, "difficulty": "Intermediate", "icon_char": "Sw", "color": "#FA7343"},
    {"name": "Kotlin", "slug": "kotlin", "quiz_count": 50, "difficulty": "Intermediate", "icon_char": "Kt", "color": "#7F52FF"},
    {"name": "C#", "slug": "csharp", "quiz_count": 50, "difficulty": "Intermediate", "icon_char": "C#", "color": "#512BD4"},
    {"name": "Dart", "slug": "dart", "quiz_count": 50, "difficulty": "Beginner", "icon_char": "Dt", "color": "#0175C2"},
    {"name": "Scala", "slug": "scala", "quiz_count": 50, "difficulty": "Advanced", "icon_char": "Sc", "color": "#DC322F"},
    {"name": "R", "slug": "r", "quiz_count": 50, "difficulty": "Intermediate", "icon_char": "R", "color": "#276DC3"},
    {"name": "Shell", "slug": "shell", "quiz_count": 50, "difficulty": "Beginner", "icon_char": "Sh", "color": "#4EAA25"},
    {"name": "SQL", "slug": "sql", "quiz_count": 50, "difficulty": "Beginner", "icon_char": "SQ", "color": "#336791"},
    {"name": "Haskell", "slug": "haskell", "quiz_count": 50, "difficulty": "Advanced", "icon_char": "Hs", "color": "#5D4F85"},
    {"name": "Elixir", "slug": "elixir", "quiz_count": 50, "difficulty": "Advanced", "icon_char": "Ex", "color": "#6E4A7E"},
    {"name": "Lua", "slug": "lua", "quiz_count": 50, "difficulty": "Intermediate", "icon_char": "Lu", "color": "#2C2D72"},
]

SITE_STATS = {
    "total_languages": 20,
    "total_quizzes": 1000,
    "total_users": 5420,
    "quizzes_taken": 38700,
}


def home(request):
    return render(request, "home.html", {
        "featured_languages": SAMPLE_LANGUAGES[:6],
        "all_languages": SAMPLE_LANGUAGES,
        "stats": SITE_STATS,
    })

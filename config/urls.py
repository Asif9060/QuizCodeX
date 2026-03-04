from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),

    # Core pages (home)
    path("", include("apps.core.urls", namespace="core")),

    # Authentication
    path("accounts/", include("apps.accounts.urls", namespace="accounts")),

    # Languages & Quizzes
    path("languages/", include("apps.languages.urls", namespace="languages")),
    path("quizzes/", include("apps.quizzes.urls", namespace="quizzes")),

    # Results
    path("results/", include("apps.results.urls", namespace="results")),

    # Leaderboard
    path("leaderboard/", include("apps.leaderboard.urls", namespace="leaderboard")),

    # Future: contests, ai_solutions, api
    # path("contests/", include("apps.contests.urls", namespace="contests")),
    # path("ai/", include("apps.ai_solutions.urls", namespace="ai_solutions")),
    # path("api/v1/", include("apps.api.urls", namespace="api_v1")),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    try:
        urlpatterns += [path("__reload__/", include("django_browser_reload.urls"))]
    except ImportError:
        pass

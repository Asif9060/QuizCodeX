from django.urls import path
from . import views

app_name = "ai_solutions"

urlpatterns = [
    # Staff-only AJAX endpoint: POST /ai/generate/<question_id>/
    path("generate/<int:question_id>/", views.generate_explanation_view, name="generate"),
]

from django.urls import path
from . import views

app_name = "quizzes"

urlpatterns = [
    path("answer/", views.submit_answer_view, name="submit_answer"),
    path("<int:result_pk>/complete/", views.complete_quiz_view, name="complete"),
    path("<slug:slug>/", views.quiz_take, name="take"),
]

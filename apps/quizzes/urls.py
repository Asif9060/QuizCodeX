from django.urls import path
from . import views

app_name = "quizzes"

urlpatterns = [
    path("<slug:slug>/", views.quiz_take, name="take"),
]

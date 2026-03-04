from django.urls import path
from . import views

app_name = "languages"

urlpatterns = [
    path("", views.language_list, name="list"),
    path("<slug:slug>/", views.language_detail, name="detail"),
]

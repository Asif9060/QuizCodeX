from django.urls import path
from . import views

app_name = "results"

urlpatterns = [
    path("<int:pk>/", views.result_detail, name="detail"),
]

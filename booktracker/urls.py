
from booktracker import views
from django.urls import path

urlpatterns = [path("", views.IndexView.as_view(), name="index")]

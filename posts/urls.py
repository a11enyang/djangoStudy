from .views import HomePageView
from django.urls import path

urlpatterns = [
    path('post/', HomePageView.as_view(), name="post"),
]
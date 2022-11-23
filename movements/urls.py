from .views import PostMovementView
from django.urls import path

urlpatterns = [
    path('movement/', PostMovementView.as_view()),
]
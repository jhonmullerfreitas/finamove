from .views import ListStoreView
from django.urls import path

urlpatterns = [
    path('stores/', ListStoreView.as_view()),
]
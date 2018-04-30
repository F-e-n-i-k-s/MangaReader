from django.contrib import admin
from django.urls import path

from .views import MangaList

urlpatterns = [
    path('manga/', MangaList.as_view()),
]

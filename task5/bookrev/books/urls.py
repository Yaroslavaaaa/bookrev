from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('book/<slug:book_slug>/', book),
]
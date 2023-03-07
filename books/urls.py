from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('book/<slug:book_slug>/', book),
    path('add', add, name="add"),
]
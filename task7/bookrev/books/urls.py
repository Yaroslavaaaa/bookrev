from django.urls import path

from .views import *

urlpatterns = [
    path('', BookHome.as_view(), name="index"),
    path('book/<slug:book_slug>/', ShowBook.as_view(), name="show_book"),
    path('genre/<slug:genre_slug>/', BookGenre.as_view(), name='genre'),
    path('add/', AddBook.as_view(), name="add"),
]
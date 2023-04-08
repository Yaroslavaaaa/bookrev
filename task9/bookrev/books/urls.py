from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *



urlpatterns = [
    path('', BookHome.as_view(), name="index"),
    path('book/<slug:book_slug>/', ShowBook.as_view(), name="show_book"),
    path('genre/<slug:genre_slug>/', BookGenre.as_view(), name='genre'),
    path('add/', AddBook.as_view(), name="add"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', logout_user, name='logout'),
    path('register/', Register.as_view(), name="register"),
    path('search/', SearchResultsView.as_view(), name='search_results'),
]


# urlpatterns = [
#     path('', cache_page(60)(BookHome.as_view()), name="index"),
#     path('book/<slug:book_slug>/', ShowBook.as_view(), name="show_book"),
#     path('genre/<slug:genre_slug>/', cache_page(60)(BookGenre.as_view()), name='genre'),
#     path('add/', AddBook.as_view(), name="add"),
#     path('login/', Login.as_view(), name="login"),
#     path('logout/', logout_user, name='logout'),
#     path('register/', Register.as_view(), name="register"),
# ]
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext


# Create your views here.
from .models import *


def index(request):
    # return HttpResponse("Страница книг")
    books = Books.objects.all()
    genres = Genres.objects.all()
    return render(request, "books/index.html", {'books': books, 'genres': genres, 'title': 'Главная страница'})
def book(request, book_slug):

    book = get_object_or_404(Books, slug=book_slug)

    context = {
        'book': book,
        'title': book.title
    }

    return render(request, "books/book.html", context=context)
    # return HttpResponse(f"Страница книг, {bid}")

def error404(request, exeption):
    return HttpResponseNotFound(f"<h1>Страница не найдена</h1>")

def error500(request):
    return HttpResponseNotFound("<h1>Ошибка сервера</h1>")

def error400(request, exeption):
    return HttpResponseNotFound("<h1>Некорректный запрос</h1>")

def error403(request, exeption):
    return HttpResponseNotFound("<h1>Доступ запрещен</h1>")

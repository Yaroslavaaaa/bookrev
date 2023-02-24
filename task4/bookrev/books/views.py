from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template import RequestContext


# Create your views here.
from .models import *


def index(request):
    # return HttpResponse("Страница книг")
    books = Books.objects.all()
    return render(request, "books/index.html", {'books': books, 'title': 'Главная страница'})
def book(request, bid):
    return  render(request, "books/index.html")
    # return HttpResponse(f"Страница книг, {bid}")

def error404(request, exeption):
    return HttpResponseNotFound(f"<h1>Страница не найдена</h1>")

def error500(request):
    return HttpResponseNotFound("<h1>Ошибка сервера</h1>")

def error400(request, exeption):
    return HttpResponseNotFound("<h1>Некорректный запрос</h1>")

def error403(request, exeption):
    return HttpResponseNotFound("<h1>Доступ запрещен</h1>")

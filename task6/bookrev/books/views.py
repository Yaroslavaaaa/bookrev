from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
# Create your views here.
from .models import *





class BookHome(ListView):
    model = Books
    template_name = 'books/index.html'
    context_object_name = 'books'
    # extra_context =

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Главная страница"
        context['genres'] = Genres.objects.all()
        context['genre_selected'] = 0
        return context


class BookGenre(ListView):
    model = Books
    template_name = 'books/index.html'
    context_object_name = 'books'
    allow_empty = False


    def get_queryset(self):
        return Books.objects.filter(genre__slug=self.kwargs['genre_slug'])


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Категория - " + str(context['books'][0].genre)
        context['genres'] = Genres.objects.all()
        context['genre_selected'] = context['books'][0].genre_id
        return context




class ShowBook(DetailView):
    model = Books
    template_name = 'books/book.html'
    slug_url_kwarg = 'book_slug'
    context_object_name = 'book'





class AddBook(CreateView):
    form_class = AddBookForm
    template_name = 'books/add.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Добавление книги"
        return context





def error404(request, exeption):
    return HttpResponseNotFound(f"<h1>Страница не найдена</h1>")

def error500(request):
    return HttpResponseNotFound("<h1>Ошибка сервера</h1>")

def error400(request, exeption):
    return HttpResponseNotFound("<h1>Некорректный запрос</h1>")

def error403(request, exeption):
    return HttpResponseNotFound("<h1>Доступ запрещен</h1>")

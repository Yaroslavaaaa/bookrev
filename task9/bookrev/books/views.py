from urllib import request

from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView


from .forms import *
# Create your views here.
from .models import *
from .utils import *





class BookHome(DataMixin, ListView):
    model = Books
    template_name = 'books/index.html'
    context_object_name = 'books'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        g_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(g_def.items()))

    def get_queryset(self):
        return Books.objects.filter(is_published=True).select_related('genre')

    # def get_queryset(self):
    #     return Books.objects.filter.select_related('genre')


class BookGenre(DataMixin, ListView):
    model = Books
    template_name = 'books/index.html'
    context_object_name = 'books'
    allow_empty = False


    def get_queryset(self):
        return Books.objects.filter(genre__slug=self.kwargs['genre_slug'], is_published=True).select_related('genre')


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # g = Books.objects.get(slug=self.kwargs['genre_slug'])
        g = get_object_or_404(Genres, slug=self.kwargs['genre_slug'])
        g_def = self.get_user_context(title='Категория - ' + str(g.genre_name),
                                      genre_selected=g.pk)
        # g_def = self.get_user_context(title="Категория - " + str(context['books'][0].genre),
        #                               genre_selected=context['books'][0].genre_id)
        return dict(list(context.items()) + list(g_def.items()))




class ShowBook(DataMixin, DetailView):
    model = Books
    form_class = CommentForm
    template_name = 'books/book.html'
    slug_url_kwarg = 'book_slug'
    context_object_name = 'book'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comments.objects.all()
        g_def = self.get_user_context(title=context['book'])
        # user = self.request.user
        return dict(list(context.items()) + list(g_def.items()))

    def form_valid(self, form):
        form.user = self.request.user.id
        form.book = get_object_or_404(Books, slug=self.kwargs['book_slug'])


        comment = form.save()
        # login(self.request, comment)
        # return redirect('index')


class AddBook(DataMixin, CreateView):
    form_class = AddBookForm
    template_name = 'books/add.html'
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('index')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        g_def = self.get_user_context(title="Добавление книги")
        return dict(list(context.items()) + list(g_def.items()))

class Register(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'books/register.html'
    success_url = reverse_lazy('login')
    # raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        g_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(g_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class Login(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'books/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('index')


class SearchResultsView(DataMixin, ListView):
    model = Books
    template_name = 'books/index.html'
    context_object_name = 'books'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        books = Books.objects.filter(
            Q(title__icontains=query) | Q(title__icontains=query)
        )
        return books

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        g_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(g_def.items()))

class AddComment(DataMixin, CreateView):
    # form_class = CommentForm
    template_name = 'books/book.html'
    success_url = reverse_lazy('book')

    # raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        g_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(g_def.items()))

    def form_valid(self, form):

        comment = form.save()
        login(self.request, comment)
        return redirect('index')


def logout_user(request):
    logout(request)
    return redirect('login')




def error404(request, exeption):
    return HttpResponseNotFound(f"<h1>Страница не найдена</h1>")

def error500(request):
    return HttpResponseNotFound("<h1>Ошибка сервера</h1>")

def error400(request, exeption):
    return HttpResponseNotFound("<h1>Некорректный запрос</h1>")

def error403(request, exeption):
    return HttpResponseNotFound("<h1>Доступ запрещен</h1>")

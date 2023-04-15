from urllib import request

from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.http import HttpResponseNotFound, Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import *
# Create your views here.
from .models import *
from .serializers import BooksSerializer
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



class BookGenre(DataMixin, ListView):
    model = Books
    template_name = 'books/index.html'
    context_object_name = 'books'
    allow_empty = False


    def get_queryset(self):
        return Books.objects.filter(genre__slug=self.kwargs['genre_slug'], is_published=True).select_related('genre')


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        g = get_object_or_404(Genres, slug=self.kwargs['genre_slug'])
        g_def = self.get_user_context(title='Категория - ' + str(g.genre_name),
                                      genre_selected=g.pk)
        return dict(list(context.items()) + list(g_def.items()))




class ShowBook(DataMixin, DetailView):
    model = Books
    template_name = 'books/book.html'
    slug_url_kwarg = 'book_slug'
    context_object_name = 'book'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()
        comments = book.comments.filter()
        context['comments'] = comments
        g_def = self.get_user_context(title=context['book'])
        context['form'] = CommentForm()

        return dict(list(context.items()) + list(g_def.items()))



class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comments
    form_class = CommentForm
    template_name = 'comment_form.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        book = get_object_or_404(Books, pk=self.kwargs['pk'])
        form.instance.user = self.request.user
        form.instance.book = book
        return super().form_valid(form)


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
    form_class = RegisterForm
    template_name = 'books/register.html'
    success_url = reverse_lazy('login')

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

class CreateComment(DataMixin, CreateView):
    model = Comments
    form_class = CommentForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        # form.instance.book_id = self.kwargs.get('slug')
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.book.get_absolute_url()


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        g_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(g_def.items()))



class UserProfile(DataMixin, DetailView):
    model = CustomUser
    template_name = "books/profile.html"
    username_url_kwarg = 'user_username'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return CustomUser.objects.get(username=self.kwargs['user_username'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['user'] = user
        g_def = self.get_user_context(title=context['user'])

        return dict(list(context.items()) + list(g_def.items()))


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        g_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(g_def.items()))



def logout_user(request):
    logout(request)
    return redirect('login')










class BooksAPIView(APIView):
    def get(self, request):
        b = Books.objects.all()
        return Response({'books': BooksSerializer(b, many=True).data})

    def post(self, request):
        serializer = BooksSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})


    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return  Response({"error": "Method PUT not allowed"})


        try:
            instance = Books.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = BooksSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"book": serializer.data})


    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})

        try:
            book = Books.objects.get(pk=pk)
            book.delete()
        except:
            return Response({"error": "Object does not exists"})

        return Response({"post": "delete post " + str(pk)})


# class BooksAPIView(generics.ListAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BooksSerializer




def error404(request, exeption):
    return HttpResponseNotFound(f"<h1>Страница не найдена</h1>")

def error500(request):
    return HttpResponseNotFound("<h1>Ошибка сервера</h1>")

def error400(request, exeption):
    return HttpResponseNotFound("<h1>Некорректный запрос</h1>")

def error403(request, exeption):
    return HttpResponseNotFound("<h1>Доступ запрещен</h1>")

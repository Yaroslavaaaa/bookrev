from django import forms
from .models import *


class AddBookForm(forms.Form):
    title = forms.CharField(max_length=255, label="Название")
    author = forms.CharField(max_length=255, label="Автор")
    slug = forms.SlugField(max_length=255, label="URL")
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label="Описание")
    genre = forms.ModelChoiceField(queryset=Genres.objects.all(), label="Жанр", empty_label="Жанр не выбран")
    pub_date = forms.IntegerField(max_value=9999, label="Дата публикации")

from django import forms
from django.core.exceptions import ValidationError

from .models import *


class AddBookForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['genre'].empty_label = "Жанр не выбран"
    class Meta:
        model = Books
        fields = ['title', 'author', 'genre', 'description', 'pub_date', 'slug', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form_input'}),
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }


    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')

        return title

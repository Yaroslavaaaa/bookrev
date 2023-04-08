from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField

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


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    capatcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class CommentForm(forms.Form):
    comment_text = forms.CharField(widget=forms.TextInput(attrs={'class': 'comment-input'}))
    user = forms.IntegerField(widget=forms.HiddenInput)
    book = forms.IntegerField(widget=forms.HiddenInput)
    parent_comment = forms.IntegerField(widget=forms.HiddenInput)

    class Meta:
        model = Comments
        fields = ('comment_text', 'user', 'book', 'parent_comment')


    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
        # self.fields['user'].empty_label =


    # parent_comment = forms.IntegerField(
    #     widget=forms.HiddenInput,
    #     required=False
    # )

    # user = forms.IntegerField(
    #     widget=forms.HiddenInput,
    #     required=False
    # )

    # comment_area = forms.CharField(
    #     label="",
    #     widget=forms.Textarea
    # )
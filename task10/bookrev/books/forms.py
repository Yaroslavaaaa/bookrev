from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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
            'title': forms.TextInput(attrs={'class': 'add-input', 'placeholder': 'Название'}),
            'author': forms.TextInput(attrs={'class': 'add-input', 'placeholder': 'Автор'}),
            'pub_date': forms.NumberInput(attrs={'class': 'add-input', 'placeholder': 'Дата публикации'}),
            'slug': forms.TextInput(attrs={'class': 'add-input', 'placeholder': 'Слаг'}),
            'genre': forms.Select(attrs={'class': 'add-select'}),
            'image': forms.FileInput(attrs={'class': 'add-input'}),
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10, 'class': 'add-description', 'placeholder': 'Описание'})
        }


    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')

        return title


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-input'}))
    username = forms.CharField(label='Nickname', widget=forms.TextInput(attrs={'class': 'form-input'}))
    age = forms.IntegerField(label='Возраст', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    capatcha = CaptchaField()

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'age', 'email', 'password1', 'password2')



class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('com_text',)
        widgets = {
            'com_text': forms.TextInput(attrs={'placeholder': 'Введите комментарий', 'class': 'input-comment'}),
        }

class EditProfileForm:
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-input'}))
    username = forms.CharField(label='Nickname', widget=forms.TextInput(attrs={'class': 'form-input'}))
    age = forms.IntegerField(label='Возраст', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    avatar = forms.FileField(label="Аватар", widget=forms.FileInput(attrs={'class': 'avatar-input'}))

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'age', 'email', 'avatar')

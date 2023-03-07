from django.db import models
from django.urls import reverse


# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    author = models.CharField(max_length=255)
    genre = models.ForeignKey("Genres", on_delete=models.PROTECT)
    description = models.TextField()
    pub_date = models.IntegerField()
    image = models.ImageField(upload_to="photos/bookphoto/%Y/%m/%d/")
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book', kwargs={'book_slug': self.slug})

    class Meta:
        verbose_name = 'Книги'
        verbose_name_plural = 'Книги'
        ordering = ['title']


class Genres(models.Model):
    genre_name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)


    def __str__(self):
        return self.genre_name


    def get_absolute_url(self):
        return reverse('genre', kwargs={'genre_id': self.pk})


    class Meta:
        verbose_name = 'Жанры'
        verbose_name_plural = 'Жанры'
        ordering = ['id']

class Users(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    surname = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to="photos/avatars/%Y/%m/%d/")
    role = models.ForeignKey("Roles", on_delete=models.PROTECT)

class Roles(models.Model):
    role_name = models.CharField(max_length=30, db_index=True)

class Comments(models.Model):
    com_text = models.TextField(db_index=True)
    book = models.ForeignKey("Books", on_delete=models.PROTECT)
    user = models.ForeignKey("Users", on_delete=models.PROTECT)
    create_time = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey("Comments", on_delete=models.PROTECT)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

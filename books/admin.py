from django.contrib import admin

# Register your models here.

from .models import *

class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'genre', 'image')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    prepopulated_fields = {"slug": ("title",)}


class GenresAdmin(admin.ModelAdmin):
    list_display = ('id', 'genre_name')
    list_display_links = ('id', 'genre_name')
    search_fields = ('genre_name',)
    prepopulated_fields = {"slug": ("genre_name",)}

admin.site.register(Books, BooksAdmin)
admin.site.register(Genres, GenresAdmin)
admin.site.register(Comments)




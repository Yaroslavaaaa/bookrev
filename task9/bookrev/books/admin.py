from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.

from .models import *

class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'genre', 'get_html_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    prepopulated_fields = {"slug": ("title",)}
    fields = ('title', 'slug', 'genre', 'description', 'author', 'image', 'is_published', 'pub_date', 'get_html_photo')
    readonly_fields = ('get_html_photo', )
    save_on_top = True

    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50>")

    get_html_photo.short_description = "Миниатюра"


class GenresAdmin(admin.ModelAdmin):
    list_display = ('id', 'genre_name')
    list_display_links = ('id', 'genre_name')
    search_fields = ('genre_name',)
    prepopulated_fields = {"slug": ("genre_name",)}



class EmployeeInline(admin.StackedInline):
    model = Users
    can_delete = False
    verbose_name_plural = 'employee'




admin.site.register(Books, BooksAdmin)
admin.site.register(Genres, GenresAdmin)
admin.site.register(Comments)

admin.site.site_title = 'Админ-панель книжного сайта'
admin.site.site_header = 'Админ-панель книжного сайта'




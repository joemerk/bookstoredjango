#adapted from https://github.com/guinslym/django-by-example-book
from django.contrib import admin
from .models import Book, Author, Genre

class GenreAdmin(admin.ModelAdmin):
    list_display = ['genre', 'slug']
    prepopulated_fields = {'slug': ('genre',)}
admin.site.register(Genre, GenreAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'authors', 'genre', 'price', 'stock', 'available', 'publication_date']
    list_filter = ['available', 'publication_date', 'genre']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Book, BookAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'slug']
    prepopulated_fields = {'slug': ('last_name',)}
admin.site.register(Author, AuthorAdmin)

from django.contrib import admin

from . models import Book, Import_Book, Comment_Book

# Register your models here.

admin.site.register(Import_Book)


class Book_Admin(admin.ModelAdmin):
    list_display = ('name', 'display_author', 'display_genre', 'price')
    search_fields = ('name', 'author__name', 'genre__name', 'price')
    list_filter = ('author__name', 'genre__name')
admin.site.register(Book, Book_Admin)


class Comment_Book_Admin(admin.ModelAdmin):
    list_display = ('book', 'rating', 'user', 'role_user')
    search_fields = ('book__name', 'rating', 'user__username')
    list_filter = ('rating', )
admin.site.register(Comment_Book, Comment_Book_Admin)

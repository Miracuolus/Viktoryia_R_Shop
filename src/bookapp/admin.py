from django.contrib import admin

from . models import Book, Import_Book, Comment_Book

# Register your models here.

admin.site.register(Import_Book)


class Book_Admin(admin.ModelAdmin):
    list_display = ('name', 'display_author', 'display_genre', 'price')
admin.site.register(Book, Book_Admin)


class Comment_Book_Admin(admin.ModelAdmin):
    list_display = ('book', 'rating', 'user', 'role_user')
admin.site.register(Comment_Book, Comment_Book_Admin)

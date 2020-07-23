from django.contrib import admin

from . models import Book, Import_Book, Comment_Book

# Register your models here.

admin.site.register(Import_Book)

admin.site.register(Comment_Book)

class Book_Admin(admin.ModelAdmin):
    list_display = ('name', 'display_author', 'display_genre', 'price')
admin.site.register(Book, Book_Admin)
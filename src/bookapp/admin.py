from django.contrib import admin

from . models import Book, Import_Book, Comment_Book

# Register your models here.

admin.site.register(Book)

admin.site.register(Import_Book)

admin.site.register(Comment_Book)
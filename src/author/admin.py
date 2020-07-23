from django.contrib import admin

# Register your models here.
from . models import Author, Import_Author

admin.site.register(Import_Author)


class Author_Admin(admin.ModelAdmin):
    list_display = ('name', 'date')
    search_fields = ('name', 'date')
admin.site.register(Author, Author_Admin)
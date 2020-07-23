from django.contrib import admin
from . models import Genre, Import_Genre

# Register your models here.

admin.site.register(Import_Genre)


class Genre_Admin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
admin.site.register(Genre, Genre_Admin)
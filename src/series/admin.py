from django.contrib import admin
from . models import Series, Import_Series

# Register your models here.

admin.site.register(Import_Series)


class Series_Admin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
admin.site.register(Series, Series_Admin)
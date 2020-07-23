from django.contrib import admin

from . models import Publisher, Import_Publisher
# Register your models here.
admin.site.register(Import_Publisher)


class Publisher_Admin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
admin.site.register(Publisher, Publisher_Admin)
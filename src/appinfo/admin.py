from django.contrib import admin

# Register your models here.
from . models import AppInfo, Import_AppInfo, Rate_Currency

admin.site.register(AppInfo)
admin.site.register(Import_AppInfo)


class Rate_Currency_Admin(admin.ModelAdmin):
    list_display = ('created', 'USD', 'EUR', 'RUB')
    search_fields = ('created',)
admin.site.register(Rate_Currency, Rate_Currency_Admin)
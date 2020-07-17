from django.contrib import admin

# Register your models here.
from . models import AppInfo, Import_AppInfo

admin.site.register(AppInfo)
admin.site.register(Import_AppInfo)
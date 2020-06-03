from django.contrib import admin
from . models import Parser, Brouser, Bot

# Register your models here.
admin.site.register(Parser)
admin.site.register(Brouser)
admin.site.register(Bot)
from django.contrib import admin

# Register your models here.
from . models import Author, Import_Author

admin.site.register(Author)
admin.site.register(Import_Author)

from django.contrib import admin

from . models import Cart, BooktoCart

# Register your models here.

admin.site.register(BooktoCart)


class Cart_Admin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'active')
admin.site.register(Cart, Cart_Admin)
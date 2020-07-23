from django.contrib import admin

from . models import Cart, BooktoCart

# Register your models here.

class Cart_Admin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'active')
    search_fields = ('pk', 'user__username')
    list_filter = ('active', )
admin.site.register(Cart, Cart_Admin)


class BooktoCart_Admin(admin.ModelAdmin):
    list_display = ('cart', 'book', 'quantity')
    search_fields = ('cart__pk', 'cart__user__username', 'book__name', 'quantity')
admin.site.register(BooktoCart, BooktoCart_Admin)
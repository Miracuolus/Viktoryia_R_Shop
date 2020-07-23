from django.contrib import admin
from .models import Order, Comment_Order

# Register your models here.

class Order_Admin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'price', 'status')
    search_fields = ('pk', 'user__username', 'price', 'status')
    list_filter = ('status', )

admin.site.register(Order, Order_Admin)


class Comment_Order_Admin(admin.ModelAdmin):
    list_display = ('order', 'user', 'role_user')
    search_fields = ('order__pk', 'user__username')
admin.site.register(Comment_Order, Comment_Order_Admin)
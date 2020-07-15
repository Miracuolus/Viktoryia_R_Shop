from django.contrib import admin
from .models import Order, Comment_Order

# Register your models here.
admin.site.register(Order)
admin.site.register(Comment_Order)

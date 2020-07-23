from django.contrib import admin
from . models import Customer
# Register your models here.

class Customer_Admin(admin.ModelAdmin):
    list_display = ('user', 'group')
    search_fields = ('user__username', )
admin.site.register(Customer, Customer_Admin)
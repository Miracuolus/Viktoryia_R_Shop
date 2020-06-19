from django.urls import path, include
from  . views import CustomerList, UpdateCustomer, CreateCustomer
app_name = 'customer'

urlpatterns = [
    path('create/', CreateCustomer.as_view(), name='create'),
    path('update/<int:user_pk>', UpdateCustomer.as_view(), name='update'),
    path('list/', CustomerList.as_view(), name='list'),
]
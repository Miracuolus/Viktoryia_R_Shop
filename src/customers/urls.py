from django.urls import path, include
from  . views import CustomerList, UpdateCustomer, CreateCustomer, DeleteCustomer, DetailCustomer
app_name = 'customer'

urlpatterns = [
    path('create/', CreateCustomer.as_view(), name='create'),
    path('update/<int:user_pk>', UpdateCustomer.as_view(), name='update'),
    path('delete/<int:pk>', DeleteCustomer.as_view(), name='delete'),
    path('detail/<int:pk>', DetailCustomer.as_view(), name='detail'),
    path('list/', CustomerList.as_view(), name='list'),
]
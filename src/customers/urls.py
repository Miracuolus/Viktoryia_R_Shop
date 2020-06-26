from django.urls import path, include
from  . views import (CustomerList,
                      UpdateMainCustomer, 
                      UpdateCustomer, 
                      CreateCustomer, 
                      DeleteCustomer, 
                      DetailCustomer,
                      ChangePasswordViewCustomer,
                      ChangePasswordDoneCustomer,
)

app_name = 'customer'

urlpatterns = [
    path('create/', CreateCustomer.as_view(), name='create'),
    path('updatemain/<int:user_pk>', UpdateMainCustomer.as_view(), name='updatemain'),
    path('update/<int:pk>', UpdateCustomer.as_view(), name='update'),
    path('delete/<int:user_pk>', DeleteCustomer.as_view(), name='delete'),
    path('detail/<int:pk>', DetailCustomer.as_view(), name='detail'),
    path('list/', CustomerList.as_view(), name='list'),
    path('change_password_view/', ChangePasswordViewCustomer.as_view(), name='change_password_view'),
    path('change_password_done/', ChangePasswordDoneCustomer.as_view(), name='password_change_done'),
    
]
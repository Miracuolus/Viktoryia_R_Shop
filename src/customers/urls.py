from django.urls import path, include
from  . views import (CustomerList,
                      UpdateMainCustomerAdmin,
                      UpdateMainCustomerUser,
                      UpdateCustomer, 
                      CreateCustomer, 
                      DeleteCustomer, 
                      DetailCustomer,
                      ChangePasswordViewCustomer,
                      ChangePasswordDoneCustomer,
                      DeleteCustomerDone,
)

app_name = 'customer'

urlpatterns = [
    path('create/', CreateCustomer.as_view(), name='create'),
    path('updatemainadmin/<int:pk>', UpdateMainCustomerAdmin.as_view(), name='updatemainadmin'),
    path('updatemainuser/<int:pk>', UpdateMainCustomerUser.as_view(), name='updatemainuser'),
    path('update/<int:pk>', UpdateCustomer.as_view(), name='update'),
    path('delete/<int:pk>', DeleteCustomer.as_view(), name='delete'),
    path('delete_done/<int:pk>', DeleteCustomerDone.as_view(), name='done'), #
    path('detail/<int:pk>', DetailCustomer.as_view(), name='detail'),
    path('list/', CustomerList.as_view(), name='list'),
    path('change_password_view/', ChangePasswordViewCustomer.as_view(), name='change_password_view'),
    path('change_password_done/', ChangePasswordDoneCustomer.as_view(), name='password_change_done'),
    
]
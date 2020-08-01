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
from .apiviews import CustomerViewSets
from rest_framework import routers


router = routers.DefaultRouter()
router.register('customer', CustomerViewSets)

app_name = 'customer'

urlpatterns = [
    path('create/', CreateCustomer.as_view(), name='create'),
    path('updatemainadmin/<int:user_pk>', UpdateMainCustomerAdmin.as_view(), name='updatemainadmin'),
    path('updatemainuser/<int:user_pk>', UpdateMainCustomerUser.as_view(), name='updatemainuser'),
    path('update/<int:user_pk>', UpdateCustomer.as_view(), name='update'), #
    path('delete/<int:pk>', DeleteCustomer.as_view(), name='delete'),
    path('delete_done/<int:user_pk>', DeleteCustomerDone.as_view(), name='done'),
    path('detail/<int:pk>', DetailCustomer.as_view(), name='detail'),
    path('list/', CustomerList.as_view(), name='list'),
    path('change_password_view/', ChangePasswordViewCustomer.as_view(), name='change_password_view'),
    path('change_password_done/', ChangePasswordDoneCustomer.as_view(), name='password_change_done'),
    path('api/', include(router.urls)),
]
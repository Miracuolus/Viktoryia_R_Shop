from django.urls import path, include
from cart.views import (AddBooktoCart,
                        ListCart,
)

app_name = 'cart'

urlpatterns = [
    path('add/', AddBooktoCart.as_view(), name='add'),
    path('list/', ListCart.as_view(), name='list'),
]

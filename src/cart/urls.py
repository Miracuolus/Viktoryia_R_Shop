from django.urls import path, include
from cart.views import (AddBooktoCart,
)

app_name = 'cart'

urlpatterns = [
    path('add/', AddBooktoCart.as_view(), name='add'),
]

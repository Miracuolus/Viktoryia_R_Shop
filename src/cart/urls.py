from django.urls import path, include
from cart.views import (AddBooktoCart,
                        ListCart,
                        UpdateBookCart,
                        DeleteBookCart,
                        DeleteCart,
)

app_name = 'cart'

urlpatterns = [
    path('add/', AddBooktoCart.as_view(), name='add'),
    path('list/', ListCart.as_view(), name='list'),
    path('update/', UpdateBookCart.as_view(), name='update'),
    path('delete/', DeleteBookCart.as_view(), name='delete'),
    path('deletecart/', DeleteCart.as_view(), name='deletecart'),
]

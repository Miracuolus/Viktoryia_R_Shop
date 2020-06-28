from django.urls import path, include
from cart.views import (CreateCart, 
                        UpdateCart, 
                        DeleteCart, 
                        DetailCart,
)

app_name = 'cart'

urlpatterns = [
    path('create/', CreateCart.as_view(), name='create'),
    path('update/<int:pk>', UpdateCart.as_view(), name='update'),
    path('deletegenre/<int:pk>', DeleteCart.as_view(), name='delete'),
    path('detail/<int:pk>', DetailCart.as_view(), name='detail'),
]


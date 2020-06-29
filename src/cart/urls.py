from django.urls import path, include
from cart.views import (CreateCart, 
                        UpdateCart, 
                        DeleteCart, 
                        ListCart,
                        AddBooktoCart,
)

app_name = 'cart'

urlpatterns = [
    #path('create/', CreateCart.as_view(), name='create'),
    #path('update/<int:pk>', UpdateCart.as_view(), name='update'),
    #path('deletegenre/<int:pk>', DeleteCart.as_view(), name='delete'),
    path('add/', ListCart.as_view(), name='add'),
    path('list/', AddBooktoCart.as_view(), name='list'),
]

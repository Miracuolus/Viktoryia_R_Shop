from django.urls import path, include
from order.views import (UpdateOrder,
)

app_name = 'order'

urlpatterns = [
    #path('detail/', AddBooktoCart.as_view(), name='detail'),
    #path('list/', ListCart.as_view(), name='list'),
    path('update/', UpdateOrder.as_view(), name='update'),
    #path('delete/', DeleteBookCart.as_view(), name='delete'),
]

from django.urls import path, include
from order.views import (UpdateOrder,
                         DetailOrder,
                         OrderList,
                         DeleteOrder,
)

app_name = 'order'

urlpatterns = [
    path('detail/<int:pk>', DetailOrder.as_view(), name='detail'),
    path('list/', OrderList.as_view(), name='list'),
    path('update/', UpdateOrder.as_view(), name='update'),
    path('delete/<int:pk>', DeleteOrder.as_view(), name='delete'),
]

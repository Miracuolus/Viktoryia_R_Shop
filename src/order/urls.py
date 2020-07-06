from django.urls import path, include
from order.views import (UpdateOrder,
                         DetailOrder,
                         OrderList,
                         DeleteOrder,
                         UpdateOrder_continue,
                         OrderListAdmin,
)

app_name = 'order'

urlpatterns = [
    path('detail/<int:pk>', DetailOrder.as_view(), name='detail'),
    path('list/', OrderList.as_view(), name='list'),
    path('update/', UpdateOrder.as_view(), name='update'),
    path('update/<int:pk>', UpdateOrder_continue.as_view(), name='update_order'),
    path('delete/<int:pk>', DeleteOrder.as_view(), name='delete'),
]

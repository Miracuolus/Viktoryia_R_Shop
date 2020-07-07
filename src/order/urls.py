from django.urls import path, include
from order.views import (UpdateOrder,
                         DetailOrder,
                         OrderList,
                         DeleteOrder,
                         UpdateOrder_continue,
                         OrderListAdmin,
                         UpdateOrder_continue_admin,
)

app_name = 'order'

urlpatterns = [
    path('detail/<int:pk>', DetailOrder.as_view(), name='detail'),
    path('list/', OrderList.as_view(), name='list'),
    path('update/', UpdateOrder.as_view(), name='update'),
    path('update_order/<int:pk>', UpdateOrder_continue.as_view(), name='update_order'),
    path('update_admin/<int:pk>', UpdateOrder_continue_admin.as_view(), name='update_admin'),
    path('delete/<int:pk>', DeleteOrder.as_view(), name='delete'),
]

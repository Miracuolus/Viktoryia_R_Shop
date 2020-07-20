from django.urls import path, include
from order.views import (UpdateOrder,
                         DetailOrder,
                         OrderList,
                         DeleteOrder,
                         UpdateOrder_continue,
                         OrderListAdmin,
                         UpdateOrder_continue_admin,
                         Create_Comment_Order,
                         Update_Comment_Order,
                         Delete_Comment_Order,
                         Create_Comment_Book,
                         Create_Comment_Book_Admin,
)

app_name = 'order'

urlpatterns = [
    path('detail/<int:pk>', DetailOrder.as_view(), name='detail'),
    path('list/', OrderList.as_view(), name='list'),
    path('update/', UpdateOrder.as_view(), name='update'),
    path('update_order/<int:pk>', UpdateOrder_continue.as_view(), name='update_order'),
    path('update_admin/<int:pk>', UpdateOrder_continue_admin.as_view(), name='update_admin'),
    path('delete/<int:pk>', DeleteOrder.as_view(), name='delete'),
    path('create_comment/', Create_Comment_Order.as_view(), name='create_comment'),
    path('update_comment/', Update_Comment_Order.as_view(), name='update_comment'),
    path('delete_comment/', Delete_Comment_Order.as_view(), name='delete_comment'),
    path('create_commentbook/', Create_Comment_Book.as_view(), name='create_commentbook'),
    path('create_commentbook_admin/', Create_Comment_Book_Admin.as_view(), name='create_commentbook_admin'),
]

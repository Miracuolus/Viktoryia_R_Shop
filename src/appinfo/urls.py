from django.urls import path, include
from  . views import UpdateAppInfo, DetailAppInfo, DetailAppInfoPayment, DetailAppInfoDelivery


app_name = 'appinfo'

urlpatterns = [
    path('update/<int:pk>', UpdateAppInfo.as_view(), name='update'),
    path('detail/<int:pk>', DetailAppInfo.as_view(), name='detail'),
    path('detail_payment/<int:pk>', DetailAppInfoPayment.as_view(), name='payment'),
    path('detail_delivery/<int:pk>', DetailAppInfoDelivery.as_view(), name='delivery'),
]
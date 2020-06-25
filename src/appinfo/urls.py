from django.urls import path, include
from  . views import UpdateAppInfo, DetailAppInfo


app_name = 'appinfo'

urlpatterns = [
    path('update/', UpdateAppInfo.as_view(), name='update'),
    path('detail/', DetailAppInfo.as_view(), name='detail'),
]
from django.urls import path, include
from  . views import (CreatePublisher, 
                      UpdatePublisher, 
                      PublisherList, 
                      DeletePublisher, 
                      DetailPublisher,
                      ImportPublisher,
)
from .apiviews import PublisherViewSets
from rest_framework import routers


router = routers.DefaultRouter()
router.register('publisher', PublisherViewSets)

app_name = 'publisher'

urlpatterns = [
    path('create/', CreatePublisher.as_view(), name='create'),
    path('update/<int:pk>', UpdatePublisher.as_view(), name='update'),
    path('delete/<int:pk>', DeletePublisher.as_view(), name='delete'),
    path('list/', PublisherList.as_view(), name='list'),
    path('detail/<int:pk>', DetailPublisher.as_view(), name='detail'),
    path('import/', ImportPublisher.as_view(), name='import'),
    path('api/', include(router.urls)),
]
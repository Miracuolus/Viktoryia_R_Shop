from django.urls import path, include
from  . views import (CreateSeries, 
                      UpdateSeries, 
                      SeriesList, 
                      DeleteSeries, 
                      DetailSeries,
                      ImportSeries,
)

app_name = 'series'

urlpatterns = [
    path('create/', CreateSeries.as_view(), name='create'),
    path('update/<int:pk>', UpdateSeries.as_view(), name='update'),
    path('delete/<int:pk>', DeleteSeries.as_view(), name='delete'),
    path('list/', SeriesList.as_view(), name='list'),
    path('detail/<int:pk>', DetailSeries.as_view(), name='detail'),
    path('import/', ImportSeries.as_view(), name='import'),
]
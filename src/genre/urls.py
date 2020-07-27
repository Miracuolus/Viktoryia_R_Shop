from django.urls import path, include
from  . views import (CreateGenre, 
                      UpdateGenre, 
                      GenreList, 
                      DeleteGenre, 
                      DetailGenre,
                      ImportGenre
)
from .apiviews import GenreViewSets
from rest_framework import routers


router = routers.DefaultRouter()
router.register('genre', GenreViewSets)

app_name = 'genre'

urlpatterns = [
    path('create/', CreateGenre.as_view(), name='create'),
    path('update/<int:pk>', UpdateGenre.as_view(), name='update'),
    path('delete/<int:pk>', DeleteGenre.as_view(), name='delete'),
    path('list/', GenreList.as_view(), name='list'),
    path('detail/<int:pk>', DetailGenre.as_view(), name='detail'),
    path('import/', ImportGenre.as_view(), name='import'),
    path('api/', include(router.urls)),
]
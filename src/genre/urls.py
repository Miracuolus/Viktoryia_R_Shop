from django.urls import path, include
from  . views import CreateGenre, UpdateGenre, GenreList, DeleteGenre, DetailGenre
app_name = 'genre'

urlpatterns = [
    path('create/', CreateGenre.as_view(), name='create'), # добавление элементов в таблицу Жанры
    path('update/<int:pk>', UpdateGenre.as_view(), name='update'), # обновление таблицы Жанры
    path('deletegenre/<int:pk>', DeleteGenre.as_view(), name='delete'), # удаление жанров
    path('list/', GenreList.as_view(), name='list'), # список жанров
    path('detail/<int:pk>', DetailGenre.as_view(), name='detail'), # справочник жанра
    path('', GenreList.as_view()), # список жанров
]
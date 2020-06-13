from django.urls import path, include
from  . views import CreateGenre, UpdateGenre, GenreList, DeleteGenre, DetailGenre
app_name = 'genre'

urlpatterns = [
    path('create/', CreateGenre.as_view(), name='create_genre'), # добавление элементов в таблицу Жанры
    path('update/<int:pk>', UpdateGenre.as_view(), name='update_genre'), # обновление таблицы Жанры
    path('deletegenre/<int:pk>', DeleteGenre.as_view(), name='delete_genre'), # удаление жанров
    path('list/', GenreList.as_view(), name='list_genre'), # список жанров
    path('detail/<int:pk>', DetailGenre.as_view(), name='detail_genre'), # справочник жанра
]
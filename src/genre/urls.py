from django.urls import path, include
from  . views import CreateGenre, UpdateGenre, GenreView, DeleteGenre
app_name = 'genre'

urlpatterns = [
    path('create/', CreateGenre.as_view(), name='create_genre'), # добавление элементов в таблицу Жанры
    path('update/<int:pk>', UpdateGenre.as_view()), # обновление таблицы Жанры
    path('deletegenre/<int:pk>', DeleteGenre.as_view()), # удаление жанров
    path('main/', GenreView.as_view()), # стартовая страница
    path('', GenreView.as_view()), # стартовая страница
]
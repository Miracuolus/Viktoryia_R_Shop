from django.urls import path, include
from bookapp.views import CreateBook

app_name = 'book'

urlpatterns = [
    path('create/', CreateBook.as_view(), name='create'), # добавление элементов в таблицу Жанры
    #path('update/<int:pk>', UpdateGenre.as_view(), name='update'), # обновление таблицы Жанры
    #path('deletegenre/<int:pk>', DeleteGenre.as_view(), name='delete'), # удаление жанров
    #path('list/', GenreList.as_view(), name='list'), # список жанров
    #path('detail/<int:pk>', DetailGenre.as_view(), name='detail'), # справочник жанра
]


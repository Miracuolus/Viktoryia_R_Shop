"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from bookapp.views import CreateGenre, UpdateGenre, GenreView, DeleteGenre, Test
from genre.views import CreateGenre, UpdateGenre, GenreView, DeleteGenre, Test

urlpatterns = [
    path('admin/', admin.site.urls), # БД
    path('create/', include('genre.urls',)), # добавление элементов в таблицу Жанры
    path('update/<int:pk>', include('genre.urls',)), # обновление таблицы Жанры
    path('deletegenre/<int:pk>', include('genre.urls',)), # удаление жанров
    path('main/', include('genre.urls',)), # стартовая страница
    path('', include('genre.urls',)), # стартовая страница
]

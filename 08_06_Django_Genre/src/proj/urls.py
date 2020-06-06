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
from django.urls import path
from bookapp.views import Test, CreateGenre, UpdateGenre

urlpatterns = [
    path('admin/', admin.site.urls), # БД
    #path('func/', func_request_work), # работа с БД через функцию
    #path('func/<int:pk>', func_request_work),
    path('create/', CreateGenre.as_view()), # создание жанров
    path('update/<int:pk>', UpdateGenre.as_view()), # обновление жанров

]

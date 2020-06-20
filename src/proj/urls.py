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
from django.conf import settings
from django.conf.urls.static import static
from bookapp.views import HomePage, AdminHomePage

urlpatterns = [
    path('admin/', admin.site.urls), # БД
    path('main/', HomePage.as_view(), name='main'), # home page
    path('book/', include('bookapp.urls', namespace='book')), # book app
    path('author/', include('author.urls', namespace='author')), # author app
    path('series/', include('series.urls', namespace='series')), # series app
    path('genre/', include('genre.urls', namespace='genre')), # genre app
    path('publisher/', include('publisher.urls', namespace='publisher')), # publisher app
    path('customer/', include('customers.urls', namespace='customer')), # customers app
    path('manager/', AdminHomePage.as_view(), name='main_admin'), # admin home page
    path('', HomePage.as_view()), # home page
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # для локальной разработки

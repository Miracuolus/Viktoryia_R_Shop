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
from customers.views import SignIn, LogIn, LogOut
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls, name ='admin'), # БД
    path('main/', HomePage.as_view(), name='main'), # home page
    path('book/', include('bookapp.urls', namespace='book')), # book app
    path('author/', include('author.urls', namespace='author')), # author app
    path('series/', include('series.urls', namespace='series')), # series app
    path('genre/', include('genre.urls', namespace='genre')), # genre app
    path('publisher/', include('publisher.urls', namespace='publisher')), # publisher app
    path('customer/', include('customers.urls', namespace='customer')), # customers app
    path('cart/', include('cart.urls', namespace='cart')), # cart app
    path('order/', include('order.urls', namespace='order')), # order app

    path('manager/', AdminHomePage.as_view(), name='main_admin'), # admin home page

    path('sign_in/', SignIn.as_view(), name='sign_in'), # sign_in page
    path('log_in/', LogIn.as_view(), name='log_in'), # log_in page
    path('log_out/', LogOut.as_view(), name='log_out'), # log_out page
    path('appinfo/', include('appinfo.urls', namespace='appinfo')), # log_out page

    path('', HomePage.as_view()), # home page

    path('reset_password_view/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_view.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset_password_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complite/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # для локальной разработки

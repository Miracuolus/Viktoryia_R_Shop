from django.urls import path, include
from bookapp.views import CreateBook, BookList

app_name = 'book'

urlpatterns = [
    path('create/', CreateBook.as_view(), name='create'),
    #path('update/<int:pk>', UpdateGenre.as_view(), name='update'),
    #path('deletegenre/<int:pk>', DeleteGenre.as_view(), name='delete'),
    path('list/', BookList.as_view(), name='list'),
    #path('detail/<int:pk>', DetailGenre.as_view(), name='detail'),
]


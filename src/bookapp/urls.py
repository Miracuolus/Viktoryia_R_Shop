from django.urls import path, include
from bookapp.views import CreateBook, BookList, UpdateBook, DeleteBook, DetailBook

app_name = 'book'

urlpatterns = [
    path('create/', CreateBook.as_view(), name='create'),
    path('update/<int:pk>', UpdateBook.as_view(), name='update'),
    path('deletegenre/<int:pk>', DeleteBook.as_view(), name='delete'),
    path('list/', BookList.as_view(), name='list'),
    path('detail/<int:pk>', DetailBook.as_view(), name='detail'),
]


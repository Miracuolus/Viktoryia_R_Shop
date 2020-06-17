from django.urls import path, include
from bookapp.views import CreateBook, BookList, UpdateBook, DeleteBook, DetailBook, ListContextBook

app_name = 'book'

urlpatterns = [
    path('create/', CreateBook.as_view(), name='create'),
    path('update/<int:pk>', UpdateBook.as_view(), name='update'),
    path('deletegenre/<int:pk>', DeleteBook.as_view(), name='delete'),
    path('list/', BookList.as_view(), name='list'),
    path('detail/<int:pk>', DetailBook.as_view(), name='detail'),
    path('list_new/', ListContextBook.as_view(), name='list_new'),
    path('list_popular/', ListContextBook.as_view(), name='list_popular'),
    path('list_sale/', ListContextBook.as_view(), name='list_sale'),
]


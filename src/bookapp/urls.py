from django.urls import path, include
from bookapp.views import (CreateBook, 
                           BookList, 
                           UpdateBook, 
                           DeleteBook, 
                           DetailBook, 
                           ListNewBook,
                           ListPopularBook,
                           ListSaleBook,
                           HomePage,
                           ListContextBook,
                           ImportBooks,
                           Create_Comment_Book_Admin,
                           Update_Comment_Book,
                           Delete_Comment_Book,
)


app_name = 'book'

urlpatterns = [
    path('create/', CreateBook.as_view(), name='create'),
    path('update/<int:pk>', UpdateBook.as_view(), name='update'),
    path('delete/<int:pk>', DeleteBook.as_view(), name='delete'),
    path('list/', BookList.as_view(), name='list'),
    path('detail/<int:pk>', DetailBook.as_view(), name='detail'),
    path('list_new/', ListNewBook.as_view(), name='list_new'),
    path('list_popular/', ListPopularBook.as_view(), name='list_popular'),
    path('list_sale/', ListSaleBook.as_view(), name='list_sale'),
    path('list_all_book/', ListContextBook.as_view(), name='list_all_book'),
    path('import/', ImportBooks.as_view(), name='import'),
    path('create_comment/', Create_Comment_Book_Admin.as_view(), name='create_comment'),
    path('update_comment/', Update_Comment_Book.as_view(), name='update_comment'),
    path('delete_comment/', Delete_Comment_Book.as_view(), name='delete_comment'),
]


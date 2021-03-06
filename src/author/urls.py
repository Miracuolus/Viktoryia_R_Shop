from django.urls import path, include
from  . views import (CreateAuthor, 
                      UpdateAuthor, 
                      AuthorList, 
                      DeleteAuthor, 
                      DetailAuthor,
                      ImportAuthors,
)


app_name = 'author'

urlpatterns = [
    path('create/', CreateAuthor.as_view(), name='create'),
    path('update/<int:pk>', UpdateAuthor.as_view(), name='update'),
    path('deletegenre/<int:pk>', DeleteAuthor.as_view(), name='delete'),
    path('list/', AuthorList.as_view(), name='list'),
    path('detail/<int:pk>', DetailAuthor.as_view(), name='detail'),
    path('import/', ImportAuthors.as_view(), name='import'),
]
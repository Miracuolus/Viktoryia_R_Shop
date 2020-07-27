from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book


class BookViewSets(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
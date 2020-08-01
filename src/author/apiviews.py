from rest_framework import viewsets
from .serializers import AuthorSerializer
from .models import Author


class AuthorViewSets(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
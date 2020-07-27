from rest_framework import viewsets
from .serializers import GenreSerializer
from .models import Genre


class GenreViewSets(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
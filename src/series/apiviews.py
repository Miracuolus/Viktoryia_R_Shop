from rest_framework import viewsets
from .serializers import SeriesSerializer
from .models import Series


class SeriesViewSets(viewsets.ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
from rest_framework import viewsets
from .serializers import PublisherSerializer
from .models import Publisher


class PublisherViewSets(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
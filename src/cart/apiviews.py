from rest_framework import viewsets
from .serializers import BooktoCartSerializer
from .models import BooktoCart


class BooktoCartViewSets(viewsets.ModelViewSet):
    queryset = BooktoCart.objects.all()
    serializer_class = BooktoCartSerializer
from rest_framework import viewsets
from .serializers import AppInfoSerializer
from .models import AppInfo


class AppInfoViewSets(viewsets.ModelViewSet):
    queryset = AppInfo.objects.all()
    serializer_class = AppInfoSerializer
from rest_framework import serializers
from . models import AppInfo


class AppInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppInfo
        fields = ('pk',
                  'name',
                  'image',
                  'year',
                  'description',
                  'payment',
                  'delivery',
        )
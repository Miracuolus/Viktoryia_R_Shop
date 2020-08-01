from rest_framework import serializers
from . models import Customer
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'is_active', 'password')


class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Customer
        fields = ('pk',
                  'user',
                  'code_phone',
                  'phone',
                  'country',
                  'city',
                  'index',
                  'address_1',
                  'address_2',
                  'group',
        )
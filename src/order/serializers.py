from rest_framework import serializers
from . models import Order
from customers.serializers import UserSerializer, GroupSerializer, CustomerSerializer



class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Order
        fields = ('pk',
                  'user',
                  'cart',
                  'price',
                  'code_phone',
                  'phone',
                  'country',
                  'city',
                  'index',
                  'address',
                  'status',
        )
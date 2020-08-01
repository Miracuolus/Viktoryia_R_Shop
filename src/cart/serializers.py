from rest_framework import serializers
from . models import BooktoCart, Cart


class BooktoCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooktoCart
        fields = ('pk',
                  'cart',
                  'book',
                  'quantity',
        )
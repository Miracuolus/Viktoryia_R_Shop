from rest_framework import serializers
from . models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('pk',
                  'name',
                  'photo',
                  'price',
                  'author',
                  'series',
                  'genre',
                  'year',
                  'pages',
                  'bookbinding',
                  'book_format',
                  'isbn',
                  'weight',
                  'description',
                  'short_description',
                  'age_limit',
                  'publisher',
                  'quantity',
                  'active',
                  'rating',
        )
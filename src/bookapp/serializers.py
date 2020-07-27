from rest_framework import serializers
from . models import Book
from genre.serializers import GenreSerializer
from series.serializers import SeriesSerializer


class BookSerializer(serializers.ModelSerializer):
    series = SeriesSerializer()
    #genre = GenreSerializer()
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
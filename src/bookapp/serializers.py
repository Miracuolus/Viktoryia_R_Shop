from rest_framework import serializers
from . models import Book
from author.serializers import AuthorSerializer
from genre.serializers import GenreSerializer
from publisher.serializers import PublisherSerializer
from series.serializers import SeriesSerializer


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True)
    series = SeriesSerializer()
    genre = GenreSerializer(many=True)
    publisher = PublisherSerializer()
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
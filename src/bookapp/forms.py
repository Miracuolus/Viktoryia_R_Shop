from django import forms
from . models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name',
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
                  'user',
        )
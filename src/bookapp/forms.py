from django import forms
from . models import Book

class GenreForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name',
                  'photo',
                  'price',
                  'author',
                  'genre',
                  'series',
                  'description',
        )
from django import forms
from . models import Book, Import_Book
from author.models import Author
from genre.models import Genre
from series.models import Series
from publisher.models import Publisher
import io
import csv

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
        )

class ImportBookForm(forms.ModelForm):
    class Meta:
        model = Import_Book
        fields = ('file_books',)

class ImportForm(forms.ModelForm):
    file_books = forms.FileField(
        label='Загрузка файла',
    )

    def process_file(self):
        data = io.TextIOWrapper(self.cleaned_data['file_books'].file)
        reader = csv.DictReader(data)
        for b in reader:
            author, created = Author.objects.get_or_create(
                    name = b['author1'],
                    defaults = {}
                    )
            genre, created = Genre.objects.get_or_create(
                    name = b['genre1'],
                    defaults = {}
                    )
            series, created = Series.objects.get_or_create(
                    name = b['series'],
                    defaults = {}
                    )
            publisher, created = Publisher.objects.get_or_create(
                    name = b['publisher'],
                    defaults = {}
                    )
            book, created = Book.objects.update_or_create(
                name = b['name'],
                photo = b['photo'],
                price = float(b['price']),
                #author  = author,
                series  = series,
                #genre  = genre,
                year  = b['year'],
                pages  = b['pages'],
                bookbinding  = b['bookbinding'],
                book_format  = b['book_format'],
                isbn  = b['isbn'],
                weight  = b['weight'],
                description  = b['description'],
                short_description  = b['short_description'],
                age_limit  = b['age_limit'],
                publisher  = publisher,
                #quantity  = b['quantity'],
                defaults = {}
            )
            #Book.objects.filter(name=b['name']).update(quantity = book.quantity + int(b['quantity']))
        return data
        
    class Meta:
        model = Import_Book
        fields = ('file_books', )
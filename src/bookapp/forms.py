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
            author_set = set()
            genre_set = set()
            authors = b['author'].split(', ')
            genres = b['genre'].split(', ')
            for a in range(0, len(authors)):
                author, created = Author.objects.get_or_create(
                        name = authors[a],
                        defaults = {}
                        )
                author_set.add(author)

            for g in range(0, len(genres)):
                genre, created = Genre.objects.get_or_create(
                        name = genres[g],
                        defaults = {}
                        )
                genre_set.add(genre)

            series, created = Series.objects.get_or_create(
                    name = b['series'],
                    defaults = {}
                    )
            publisher, created = Publisher.objects.get_or_create(
                    name = b['publisher'],
                    defaults = {}
                    )
            if Book.objects.filter(pk=b['\ufeffpk']).exists():
                book = Book.objects.filter(pk=b['\ufeffpk']).update(
                    name = b['name'],
                    photo = b['photo'],
                    price = float(b['price']),
                    series  = series,
                    year  = b['year'],
                    pages  = b['pages'],
                    bookbinding  = b['bookbinding'],
                    book_format  = b['book_format'],
                    isbn  = b['isbn'],
                    #weight  = b['weight'],
                    description  = b['description'],
                    short_description  = b['short_description'],
                    age_limit  = b['age_limit'],
                    publisher  = publisher,
                )
            else:
                book, created = Book.objects.update_or_create(
                    pk = b['\ufeffpk'],
                    name = b['name'],
                    photo = b['photo'],
                    price = float(b['price']),
                    series  = series,
                    year  = b['year'],
                    pages  = b['pages'],
                    bookbinding  = b['bookbinding'],
                    book_format  = b['book_format'],
                    isbn  = b['isbn'],
                    #weight  = b['weight'],
                    description  = b['description'],
                    short_description  = b['short_description'],
                    age_limit  = b['age_limit'],
                    publisher  = publisher,
                    #quantity  = b['quantity'],
                    defaults = {}
                )
            #Book.objects.filter(name=b['name']).update(quantity = book.quantity + int(b['quantity']))
            B = Book.objects.filter(name=b['name']).first()
            B.author.add(*author_set)
            B.genre.add(*genre_set)
            if b['weight']:
                B.weight = b['weight']
        return data
        
    class Meta:
        model = Import_Book
        fields = ('file_books', )
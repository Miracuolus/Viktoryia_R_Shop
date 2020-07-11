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
        count_author = 0
        author_set = set()
        count_genre = 0
        genre_set = set()
        for b in reader:

            if b['author1']:
                if b['author2']:
                    if b['author3']:
                        count_author = 3
                    else:
                        count_author = 2
                else:
                    count_author = 1
            author_list = (b['author1'], b['author2'], b['author3'])

            for a in range(0, count_author):
                author, created = Author.objects.get_or_create(
                        name = author_list[a],
                        defaults = {}
                        )
                author_set.add(author)

            if b['genre1']:
                if b['genre2']:
                    if b['genre3']:
                        count_genre = 3
                    else:
                        count_genre = 2
                else:
                    count_genre = 1
            genre_list = (b['genre1'], b['genre2'], b['genre3'])

            for g in range(0, count_genre):
                genre, created = Genre.objects.get_or_create(
                        name = genre_list[g],
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
            book, created = Book.objects.update_or_create(
                name = b['name'],
                photo = b['photo'],
                price = float(b['price']),
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
            B = Book.objects.filter(name=b['name']).first()
            B.author.add(*author_set)
            B.genre.add(*genre_set)
        return data
        
    class Meta:
        model = Import_Book
        fields = ('file_books', )
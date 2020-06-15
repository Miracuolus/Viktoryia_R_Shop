from django.db import models
from genre.models import Genre
from author.models import Author
from series.models import Series
from publisher.models import Publisher
from decimal import Decimal

# Create your models here.
class Book(models.Model):
    name = models.CharField(
        verbose_name='Название книги',
        max_length= 200
    )
    photo = models.ImageField(
        upload_to='static/book', 
        height_field=None, 
        width_field=None, 
        max_length=100,
        default = 'static/book/10912445_0.jpg'
    )
    price = models.DecimalField(
        verbose_name='Цена',
        max_digits=6,
        decimal_places=2,
        default=Decimal('0.00')
       )
    author = models.ManyToManyField(
        Author,
        verbose_name='Автор',
    )
    series = models.ForeignKey(
        Series,
        on_delete=models.PROTECT,
        verbose_name='Серия',
    )
    genre = models.ManyToManyField(
        Genre,
        verbose_name='Жанр книги',
    )
    year = models.PositiveSmallIntegerField(
        verbose_name='Год издания',
    )
    pages = models.PositiveSmallIntegerField(
        verbose_name='Кол-во страниц',
    )
    bookbinding = models.CharField(
        verbose_name='Переплет',
        max_length= 100,
        null=True,
        blank=True,
    )
    book_format = models.CharField(
        verbose_name='Формат',
        max_length= 300,
        null=True,
        blank=True,
    )
    isbn = models.SlugField(
        verbose_name='ISBN',
        max_length= 100,
        null=True,
        blank=True,
    )
    weight = models.PositiveSmallIntegerField(
        verbose_name='Вес (гр)',
        null=True,
        blank=True,
        help_text='Указывается в граммах'
    )
    description = models.TextField(
        verbose_name='Описание книги',
        null=True, # БД позволяет хранить поле пустым
        blank=True, # сигнал Djange, что поле мб пустым
        help_text='Поле может быть пустым'
    )
    age_limit = models.CharField(
        verbose_name='Возрастные ограничения',
        max_length= 100,
        default='0+'
    )
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.PROTECT,
        verbose_name='Издательство',
        null=True,
        blank=True,
    )
    quantity = models.PositiveSmallIntegerField(
        verbose_name='В наличии',
    )
    active = models.BooleanField(
        max_length=2,
        choices=((True, 'Да'),(False, 'Нет')),
        default=False
    )
    rating = models.PositiveSmallIntegerField(
        verbose_name='Рейтинг',
    )
    created = models.DateTimeField(
        verbose_name='Создано',
        auto_now=False, # автом ставить тек время
        auto_now_add=True, # автом ставить время добавления
    )
    updated = models.DateTimeField(
        verbose_name='Изменено',
        auto_now=True, # автом ставить тек время
        auto_now_add=False # автом ставить время добавления
    )
    def __str__(self):
        return f'{self.name}'

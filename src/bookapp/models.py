from django.db import models
from genre.models import Genre
from author.models import Author
from series.models import Series
from publisher.models import Publisher
from decimal import Decimal
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Book(models.Model):
    name = models.CharField(
        verbose_name='Название книги',
        max_length= 200,
        unique=True,
    )
    photo = models.ImageField(
        verbose_name='Изображение',
        upload_to='books', 
        height_field=None, 
        width_field=None,
        default = 'books/incognito.png',
    )
    price = models.DecimalField(
        verbose_name='Цена',
        max_digits=6,
        decimal_places=2,
        default=Decimal('0.00'),
    )
    author = models.ManyToManyField(
        Author,
        verbose_name='Автор',
        related_name = 'books',
    )
    series = models.ForeignKey(
        Series,
        on_delete=models.PROTECT,
        verbose_name='Серия',
        null=True,
        blank=True,
    )
    genre = models.ManyToManyField(
        Genre,
        verbose_name='Жанр книги',
        related_name = 'genrebooks',
    )
    year = models.PositiveSmallIntegerField(
        verbose_name='Год издания',
        null=True,
        blank=True,
        help_text='ГГГГ'
    )
    pages = models.PositiveSmallIntegerField(
        verbose_name='Кол-во страниц',
        null=True,
        blank=True,
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
    short_description = models.TextField(
        verbose_name='Аннотация',
        help_text='Поле может быть пустым',
        null=True,
        blank=True, #
    )
    age_limit = models.CharField(
        verbose_name='Возрастные ограничения',
        max_length= 100,
        default='0+',
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
        default=0,
    )
    active = models.BooleanField(
        max_length=2,
        choices=((True, 'Да'),(False, 'Нет')),
        default=False,
    )
    rating = models.DecimalField(
        verbose_name='Рейтинг',
        max_digits=6,
        decimal_places=1,
        help_text='от 0 до 5',
        null=True,
        blank=True,
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
    comment = models.ManyToManyField(
        'Comment_Book',
        verbose_name='Комментарии',
        blank=True,
        related_name='comments',
    )

    def display_genre(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ genre.name for genre in self.genre.all() ])
    display_genre.short_description = 'Жанры'

    def display_author(self):
        """
        Creates a string for the Author. This is required to display author in Admin.
        """
        return ', '.join([ author.name for author in self.author.all() ])
    display_author.short_description = 'Авторы'

    class Meta: 
        permissions=[('view_active_book', 'Can view active books'),
                     ('view_admin_db', 'Can view admin db'),
        ]
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class Import_Book(models.Model):
    file_books = models.FileField(
        verbose_name='Каталог товаров',
        upload_to='files',
    )

    created = models.DateTimeField(
        verbose_name='Создано',
        auto_now=False, # автом ставить тек время
        auto_now_add=True, # автом ставить время добавления
    )

    class Meta: 
        verbose_name = 'Каталог книг'
        verbose_name_plural = 'Каталоги книг'
    
    def __str__(self):
        return f'{self.created}'


class Comment_Book(models.Model):
    book = models.ForeignKey(
        'Book',
        on_delete=models.CASCADE,
        verbose_name='Книга',
        null=True,
        blank=True,
    )
    rating = models.CharField(
        verbose_name='Оценка',
        choices=(('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1'), ('0', '0')),
        max_length= 100,
        null=True,
    )
    comment = models.TextField(
        verbose_name='Комментарий',
        max_length= 100,
        null=True,
        blank=True,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name='Пользователь',
    )
    role_user = models.ForeignKey(
        Group,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name='Группа',
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

    class Meta: 
        verbose_name = 'Комментарий к книге'
        verbose_name_plural = 'Комментарии к книгам'
        #unique_together = [('user','book'),]
        ordering = ['book']
    
    def __str__(self):
        return f'Книга {self.book} - оценка {self.rating}: {self.user} - {self.role_user} - {self.created}'

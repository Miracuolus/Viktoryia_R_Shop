from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(
        verbose_name='Название жанра',
        max_length= 100,
        unique=True,
    )
    description = models.TextField(
        verbose_name='Описание жанра',
        null=True, # БД позволяет хранить поле пустым
        blank=True, # сигнал Djange, что поле мб пустым
        help_text='Поле может быть пустым'
    )

    class Meta: 
        ordering = ['name']
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
    
    def __str__(self):
        return f'{self.name}'

class Import_Genre(models.Model):
    file_genre = models.FileField(
        verbose_name='Каталог жанров',
        upload_to='files',
    )

    created = models.DateTimeField(
        verbose_name='Создано',
        auto_now=False, # автом ставить тек время
        auto_now_add=True, # автом ставить время добавления
    )

    class Meta: 
        verbose_name = 'Каталог жанров'
        verbose_name_plural = 'Каталоги жанров'
    
    def __str__(self):
        return f'{self.created}'


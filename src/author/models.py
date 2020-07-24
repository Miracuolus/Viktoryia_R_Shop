from django.db import models
import datetime

# Create your models here.
class Author(models.Model):
    name = models.CharField(
        verbose_name='Автор',
        max_length= 200,
        unique=True,
    )

    date = models.DateField(
        verbose_name='Дата рождения',
        help_text='ДД.ММ.ГГГГ',
        null=True,
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='authors',
        default = 'authors/notfound_0.png',
    )
    description = models.TextField(
        verbose_name='Биография',
        null=True,
        blank=True,
        help_text='Поле может быть пустым',
        default = '',
    )

    class Meta: 
        ordering = ['name']
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
    
    def __str__(self):
        return f'{self.name}'

class Import_Author(models.Model):
    file_author = models.FileField(
        verbose_name='Каталог авторов',
        upload_to='files',
    )

    created = models.DateTimeField(
        verbose_name='Создано',
        auto_now=False, # автом ставить тек время
        auto_now_add=True, # автом ставить время добавления
    )

    class Meta: 
        verbose_name = 'Каталог авторов'
        verbose_name_plural = 'Каталоги авторов'
    
    def __str__(self):
        return f'{self.created}'
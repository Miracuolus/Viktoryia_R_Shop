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
        null=True,
        blank=True,
    )
    description = models.TextField(
        verbose_name='Биография',
        null=True,
        blank=True,
        help_text='Поле может быть пустым'
    )

    class Meta: 
        ordering = ['name']
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
    
    def __str__(self):
        return f'{self.name}'

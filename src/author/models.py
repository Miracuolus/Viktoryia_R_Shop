from django.db import models
import datetime

# Create your models here.
class Author(models.Model):
    name = models.CharField(
        verbose_name='Автор',
        max_length= 200
    )

    date = models.DateField(
        verbose_name='Дата рождения',
        null=True,
        blank=True,
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='authors',
    )
    description = models.TextField(
        verbose_name='Биография',
        null=True,
        blank=True,
        help_text='Поле может быть пустым'
    )

    class Meta: 
        ordering = ['name']
    
    def __str__(self):
        return f'{self.name}'

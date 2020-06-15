from django.db import models
from datetime import datetime

# Create your models here.
class Author(models.Model):
    name = models.CharField(
        verbose_name='Автор',
        max_length= 200
    )

    date = models.DateField(
        verbose_name='Год рождения',
    )
    image = models.ImageField(
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
    
    def __str__(self):
        return f'{self.name}'

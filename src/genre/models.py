from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(
        verbose_name='Название жанра',
        max_length= 100
    )
    description = models.TextField(
        verbose_name='Описание жанра',
        null=True, # БД позволяет хранить поле пустым
        blank=True, # сигнал Djange, что поле мб пустым
        help_text='Поле может быть пустым'
    )

    class Meta: 
        ordering = ['name']

    def __str__(self):
        return f'Жанр {self.name}'

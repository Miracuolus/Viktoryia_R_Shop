from django.db import models

# Create your models here.
class Series(models.Model):
    name = models.CharField(
        verbose_name='Серия',
        max_length= 200,
        unique=True,
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='series',
        default = 'authors/notfound_0.png',
    )
    description = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=True,
        help_text='Поле может быть пустым'
    )

    class Meta: 
        ordering = ['name']
        verbose_name = 'Серия'
        verbose_name_plural = 'Серии'
    
    def __str__(self):
        return f'{self.name}'

class Import_Series(models.Model):
    file_series = models.FileField(
        verbose_name='Каталог серий',
        upload_to='files',
    )

    created = models.DateTimeField(
        verbose_name='Создано',
        auto_now=False, # автом ставить тек время
        auto_now_add=True, # автом ставить время добавления
    )

    class Meta: 
        verbose_name = 'Каталог серий'
        verbose_name_plural = 'Каталоги серий'
    
    def __str__(self):
        return f'{self.created}'
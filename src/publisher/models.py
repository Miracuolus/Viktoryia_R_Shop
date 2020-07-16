from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(
        verbose_name='Издательство',
        max_length= 100,
        unique=True,
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='publishers', 
        height_field=None,
        width_field=None,
        default = 'publishers/notfound_0.png',
    )
    description = models.TextField(
        verbose_name='Краткая информация об издательстве',
        null=True,
        blank=True,
        help_text='Поле может быть пустым'
    )

    class Meta: 
        ordering = ['name']
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'
    
    def __str__(self):
        return f'{self.name}'

class Import_Publisher(models.Model):
    file_publisher = models.FileField(
        verbose_name='Каталог издательств',
        upload_to='files',
    )

    created = models.DateTimeField(
        verbose_name='Создано',
        auto_now=False, # автом ставить тек время
        auto_now_add=True, # автом ставить время добавления
    )

    class Meta: 
        verbose_name = 'Каталог издательств'
        verbose_name_plural = 'Каталоги издательств'
    
    def __str__(self):
        return f'{self.created}'
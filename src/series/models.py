from django.db import models

# Create your models here.
class Series(models.Model):
    name = models.CharField(
        verbose_name='Серия',
        max_length= 200
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='series',
    )
    description = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=True,
        help_text='Поле может быть пустым'
    )

    class Meta: 
        ordering = ['name']
    
    def __str__(self):
        return f'{self.name}'
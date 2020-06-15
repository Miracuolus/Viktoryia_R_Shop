from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(
        verbose_name='Издательство',
        max_length= 100
    )
    image = models.ImageField(
        null=True,
        blank=True,
    )
    description = models.TextField(
        verbose_name='Краткая информация об издательстве',
        null=True, # БД позволяет хранить поле пустым
        blank=True, # сигнал Djange, что поле мб пустым
        help_text='Поле может быть пустым'
    )

    class Meta: 
        ordering = ['name']
    
    def __str__(self):
        return f'{self.name}'
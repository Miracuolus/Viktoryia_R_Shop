from django.db import models

# Create your models here.
class AppInfo(models.Model):
    name = models.CharField(
        verbose_name='Название магазина',
        max_length= 200,
        unique=True
    )
    image = models.ImageField(
        verbose_name='Логотип магазина',
        upload_to='logo',
        null=True,
        blank=True,
    )
    year = models.CharField(
        verbose_name='Год разработки сайта',
        help_text='ГГГГ',
        max_length= 200,
        null=True,
        blank=True,
    )
    description = models.TextField(
        verbose_name='О магазине',
        null=True,
        blank=True,
    )
    payment = models.TextField(
        verbose_name='Оплата',
        null=True,
        blank=True,
    )
    delivery = models.TextField(
        verbose_name='Доставка',
        null=True,
        blank=True,
    )

    class Meta: 
        ordering = ['name']
        verbose_name = 'О магазине'
        verbose_name_plural = 'О магазине'

    def __str__(self):
        return f'{self.name}'


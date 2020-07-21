from django.db import models
from decimal import Decimal

# Create your models here.
class AppInfo(models.Model):
    name = models.CharField(
        verbose_name='Название магазина',
        max_length= 200,
        unique=True,
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


class Import_AppInfo(models.Model):
    file_info = models.FileField(
        verbose_name='Информация о приложении',
        upload_to='files',
    )

    created = models.DateTimeField(
        verbose_name='Создано',
        auto_now=False, # автом ставить тек время
        auto_now_add=True, # автом ставить время добавления
    )

    class Meta: 
        verbose_name = 'Каталог информации о приложении'
        verbose_name_plural = 'Каталоги информации о приложении'
    
    def __str__(self):
        return f'{self.created}'

class Rate_Currency(models.Model):
    USD = models.DecimalField(
        verbose_name='USD',
        max_digits=7,
        decimal_places=4,
        default=Decimal('0.00'),
    )
    EUR = models.DecimalField(
        verbose_name='EUR',
        max_digits=7,
        decimal_places=4,
        default=Decimal('0.00'),
    )
    RUB = models.DecimalField(
        verbose_name='RUB',
        max_digits=7,
        decimal_places=4,
        default=Decimal('0.00'),
    )
    created = models.DateField(
        verbose_name='Создано',
        unique=True,
        auto_now=False, # автом ставить тек время
        auto_now_add=True, # автом ставить время добавления
    )

    class Meta: 
        verbose_name = 'Каталог курсов валют'
        verbose_name_plural = 'Каталоги курсов валют'
    
    def __str__(self):
        return f'{self.created}'

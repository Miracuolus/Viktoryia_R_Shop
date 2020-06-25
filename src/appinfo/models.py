from django.db import models

# Create your models here.
class AppInfo(models.Model):
    name = models.CharField(
        verbose_name='Название магазина',
        max_length= 200
    )
    image = models.ImageField(
        verbose_name='Логотип магазина',
        upload_to='logo',
    )
    year = models.PositiveSmallIntegerField(
        verbose_name='Год разработки сайта',
        help_text='ГГГГ'
    )
    description = models.TextField(
        verbose_name='О магазине',
    )
    payment = models.TextField(
        verbose_name='Оплата',
    )
    delivery = models.TextField(
        verbose_name='Доставка',
    )

    def __str__(self):
        return f'{self.name}'


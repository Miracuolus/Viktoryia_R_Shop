from django.db import models

from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()
class Customer(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
    )
    log = models.CharField(
        verbose_name='Логин',
        max_length= 200
    )
    password = models.SlugField(
        verbose_name='Пароль',
        max_length= 10
    )
    mail = models.EmailField(
        verbose_name='E-mail',
        max_length= 100
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length= 200,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length= 200,
        null=True,
        blank=True,
    )
    phone = models.PositiveIntegerField(
        verbose_name='Телефон',
    )
    country = models.CharField(
        verbose_name='Страна',
        max_length= 100,
        null=True,
        blank=True,
    )
    city = models.CharField(
        verbose_name='Город',
        max_length= 100,
        null=True,
        blank=True,
    )
    index = models.PositiveSmallIntegerField(
        verbose_name='Почтовый индекс',
        null=True,
        blank=True,
    )
    address_1 = models.CharField(
        verbose_name='Адрес 1',
        max_length= 200,
        null=True,
        blank=True,
    )
    address_2 = models.CharField(
        verbose_name='Адрес 2',
        max_length= 200,
        null=True,
        blank=True,
    )

    class Meta: 
        ordering = ['user']
    
    def __str__(self):
        #return f'{self.user.first_name}{self.user.last_name}'
        return f'{self.user}'

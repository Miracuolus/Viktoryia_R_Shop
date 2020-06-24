from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Customer(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
    )
    code_phone = models.SmallIntegerField(
        verbose_name='Код номера',
        choices=((8029, '(029)'),(8033, '(033)'),(8044, '(044)'),(8017, '(017)')),
        null=True,
        blank=True,
    )
    phone = models.PositiveIntegerField(
        verbose_name='Телефон',
        help_text='7 цифр',
        null=True,
        blank=True,
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
    group = models.ForeignKey(
        Group,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    class Meta:
        ordering = ['user']

    
    def __str__(self):
        #return f'{self.user.first_name}{self.user.last_name}'
        return f'{self.user}'

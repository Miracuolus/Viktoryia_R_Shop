from django.db import models
from django.contrib.auth import get_user_model
from bookapp.models import Book
from decimal import Decimal

# Create your models here.
User = get_user_model()

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.PROTECT,
    )

    book = models.ManyToManyField(
        Book,
        verbose_name='Книги',
    )
    quantity = models.PositiveSmallIntegerField(
        verbose_name='Количество',
    )
    price = models.DecimalField(
        verbose_name='Цена',
        max_digits=6,
        decimal_places=2,
        default=Decimal('0.00')
    )
    created = models.DateTimeField(
        verbose_name='Создано',
        auto_now=False, # автом ставить тек время
        auto_now_add=True, # автом ставить время добавления
    )
    updated = models.DateTimeField(
        verbose_name='Изменено',
        auto_now=True, # автом ставить тек время
        auto_now_add=False # автом ставить время добавления
    )

    class Meta: 
        ordering = ['user']
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
    
    def __str__(self):
        return f'{self.name}'


from django.db import models
from django.contrib.auth import get_user_model
from bookapp.models import Book
from decimal import Decimal

# Create your models here.
User = get_user_model()
class Cart(models.Model):
    user = models.ForeignKey(
        User,
        related_name='carts',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'Корзина #{self.pk}'

# Create your models here.
class BooktoCart(models.Model):
    cart = models.ForeignKey(
        Cart,
        related_name='books',
        on_delete=models.CASCADE,
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.PROTECT,
        related_name='book_in_cart',
    )
    quantity = models.PositiveSmallIntegerField(
        verbose_name='Количество',
        default=1,
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
        ordering = ['cart']
        unique_together = [('cart','book'),]
    
    def __str__(self):
        return f'Book #{self.book.pk} in cart #{self.cart.pk}'


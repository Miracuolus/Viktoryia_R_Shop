from django.db import models
from django.contrib.auth import get_user_model
from cart.models import Cart
from customers.models import Customer
from decimal import Decimal

# Create your models here.
User = get_user_model()
class Order(models.Model):
    user = models.ForeignKey(
        User,
        related_name='orders',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Пользователь',
    )
    cart = models.ForeignKey(
        Cart,
        related_name='cart_in_order',
        on_delete=models.CASCADE,
        verbose_name='Корзина',
    )
    price = models.DecimalField(
        verbose_name='Цена',
        max_length = 100,
        max_digits=6,
        decimal_places=2,
        default=Decimal('0.00')
    )
    code_phone = models.SmallIntegerField(
        verbose_name='Код номера',
        choices=((8029, '(029)'),(8033, '(033)'),(8044, '(044)'),(8017, '(017)')),
        null=True,
    )
    phone = models.PositiveIntegerField(
        verbose_name='Телефон',
        help_text='7 цифр',
        null=True,
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
    address = models.CharField(
        verbose_name='Адрес',
        max_length= 200,
        null=True,
        blank=True,
    )
    status = models.CharField(
        verbose_name='Статус заказа',
        choices=(('Открыт', 'Открыт'),('В обработке', 'В обработке'),('Доставка', 'Доставка'), ('Отменен', 'Отменен'),('Закрыт', 'Закрыт')),
        max_length= 100,
        default = 'Открыт',
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
        #ordering = ['status']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        unique_together = [('cart','price'),]
    
    def __str__(self):
        return f'{self.user} {self.created}, status {self.status}'


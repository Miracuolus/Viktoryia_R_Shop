from django.db import models
from django.contrib.auth import get_user_model
from cart.models import Cart
from customers.models import Customer
from decimal import Decimal
from django.contrib.auth.models import Group

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
    cart = models.OneToOneField(
        Cart,
        related_name='cart_in_order',
        on_delete=models.PROTECT,
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

    comment = models.ManyToManyField(
        'Comment_Order',
        verbose_name='Комментарии',
        blank=True,
        related_name='comments',
    )
    class Meta: 
        ordering = ['pk']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
    
    def __str__(self):
        return f'{self.user} {self.created}, status {self.status}'


class Comment_Order(models.Model):
    order = models.ForeignKey(
        'Order',
        on_delete=models.CASCADE,
        verbose_name='Заказ',
        related_name='order',
        null=True,
        blank=True,
    )
    comment = models.TextField(
        verbose_name='Комментарий',
        max_length= 100,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name='Пользователь',
    )
    role_user = models.ForeignKey(
        Group,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name='Группа',
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
        verbose_name = 'Комментарий к заказу'
        verbose_name_plural = 'Комментарии к заказам'
    
    def __str__(self):
        return f'{self.user} - {self.role_user} - {self.created}'
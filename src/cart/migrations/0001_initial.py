# Generated by Django 3.0.7 on 2020-06-29 13:50

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookapp', '0046_auto_20200627_1952'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BooktoCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=1, verbose_name='Количество')),
                ('price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=6, verbose_name='Цена')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Изменено')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='book_in_cart', to='bookapp.Book')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='cart.Cart')),
            ],
            options={
                'ordering': ['cart'],
                'unique_together': {('cart', 'book')},
            },
        ),
    ]

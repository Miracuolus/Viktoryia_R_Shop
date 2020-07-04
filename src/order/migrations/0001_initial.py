# Generated by Django 3.0.7 on 2020-07-04 15:09

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0008_auto_20200630_2253'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=6, verbose_name='Цена')),
                ('code_phone', models.SmallIntegerField(choices=[(8029, '(029)'), (8033, '(033)'), (8044, '(044)'), (8017, '(017)')], verbose_name='Код номера')),
                ('phone', models.PositiveIntegerField(help_text='7 цифр', verbose_name='Телефон')),
                ('country', models.CharField(blank=True, max_length=100, null=True, verbose_name='Страна')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='Город')),
                ('index', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Почтовый индекс')),
                ('address_1', models.CharField(blank=True, max_length=200, null=True, verbose_name='Адрес 1')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Изменено')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_in_order', to='cart.Cart')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]

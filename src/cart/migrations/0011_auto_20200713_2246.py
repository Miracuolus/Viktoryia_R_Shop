# Generated by Django 3.0.7 on 2020-07-13 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0010_cart_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Активная корзина'),
        ),
    ]

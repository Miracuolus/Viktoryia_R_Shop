# Generated by Django 3.0.7 on 2020-07-23 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0024_auto_20200721_1403'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['status'], 'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
    ]

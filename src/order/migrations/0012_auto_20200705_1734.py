# Generated by Django 3.0.7 on 2020-07-05 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_auto_20200705_1433'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['status'], 'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
    ]

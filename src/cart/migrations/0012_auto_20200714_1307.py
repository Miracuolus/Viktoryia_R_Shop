# Generated by Django 3.0.7 on 2020-07-14 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0011_auto_20200713_2246'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booktocart',
            options={'ordering': ['cart'], 'verbose_name': 'Состав корзины'},
        ),
    ]

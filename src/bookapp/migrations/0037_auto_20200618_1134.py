# Generated by Django 3.0.7 on 2020-06-18 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0036_auto_20200617_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.PositiveSmallIntegerField(help_text='от 0 до 10', verbose_name='Рейтинг'),
        ),
    ]

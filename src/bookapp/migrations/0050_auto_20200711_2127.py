# Generated by Django 3.0.7 on 2020-07-11 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0049_auto_20200711_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.PositiveSmallIntegerField(blank=True, default=0, help_text='от 0 до 10', null=True, verbose_name='Рейтинг'),
        ),
    ]
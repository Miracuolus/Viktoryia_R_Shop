# Generated by Django 3.0.7 on 2020-07-21 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0068_auto_20200721_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=1, help_text='от 0 до 5', max_digits=6, null=True, verbose_name='Рейтинг'),
        ),
        migrations.AlterField(
            model_name='comment_book',
            name='rating',
            field=models.CharField(choices=[('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1'), ('0', '0')], max_length=100, null=True, verbose_name='Оценка'),
        ),
    ]

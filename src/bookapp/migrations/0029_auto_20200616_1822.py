# Generated by Django 3.0.7 on 2020-06-16 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0001_initial'),
        ('bookapp', '0028_auto_20200616_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Кол-во страниц'),
        ),
        migrations.AlterField(
            model_name='book',
            name='series',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='series.Series', verbose_name='Серия'),
        ),
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Год издания'),
        ),
    ]

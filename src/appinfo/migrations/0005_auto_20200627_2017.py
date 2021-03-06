# Generated by Django 3.0.7 on 2020-06-27 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appinfo', '0004_auto_20200627_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appinfo',
            name='delivery',
            field=models.TextField(blank=True, null=True, verbose_name='Доставка'),
        ),
        migrations.AlterField(
            model_name='appinfo',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='О магазине'),
        ),
        migrations.AlterField(
            model_name='appinfo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='logo', verbose_name='Логотип магазина'),
        ),
        migrations.AlterField(
            model_name='appinfo',
            name='payment',
            field=models.TextField(blank=True, null=True, verbose_name='Оплата'),
        ),
        migrations.AlterField(
            model_name='appinfo',
            name='year',
            field=models.CharField(blank=True, help_text='ГГГГ', max_length=200, null=True, verbose_name='Год разработки сайта'),
        ),
    ]

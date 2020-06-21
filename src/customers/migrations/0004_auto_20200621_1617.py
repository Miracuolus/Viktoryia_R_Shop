# Generated by Django 3.0.7 on 2020-06-21 13:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customers', '0003_auto_20200620_0016'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address_1',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Адрес 1'),
        ),
        migrations.AddField(
            model_name='customer',
            name='address_2',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Адрес 2'),
        ),
        migrations.AddField(
            model_name='customer',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='customer',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Страна'),
        ),
        migrations.AddField(
            model_name='customer',
            name='first_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='customer',
            name='index',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Почтовый индекс'),
        ),
        migrations.AddField(
            model_name='customer',
            name='last_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Фамилия'),
        ),
        migrations.AddField(
            model_name='customer',
            name='log',
            field=models.CharField(default='user', max_length=200, verbose_name='Логин'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='mail',
            field=models.EmailField(default='user@mail.ru', max_length=100, verbose_name='E-mail'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.SlugField(default=1, max_length=10, verbose_name='Пароль'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.PositiveIntegerField(default=1, verbose_name='Телефон'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]

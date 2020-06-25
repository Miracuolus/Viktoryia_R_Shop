# Generated by Django 3.0.7 on 2020-06-25 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название магазина')),
                ('image', models.ImageField(upload_to='logo', verbose_name='Логотип магазина')),
                ('year', models.PositiveSmallIntegerField(help_text='ГГГГ', verbose_name='Год разработки сайта')),
                ('description', models.TextField(verbose_name='О магазине')),
                ('payment', models.TextField(verbose_name='Оплата')),
                ('delivery', models.TextField(verbose_name='Доставка')),
            ],
        ),
    ]

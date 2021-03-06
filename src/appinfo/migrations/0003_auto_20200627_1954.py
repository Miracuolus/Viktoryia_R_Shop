# Generated by Django 3.0.7 on 2020-06-27 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appinfo', '0002_auto_20200626_0043'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appinfo',
            options={'ordering': ['name'], 'verbose_name': 'О магазине', 'verbose_name_plural': 'О магазинах'},
        ),
        migrations.AlterField(
            model_name='appinfo',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='Название магазина'),
        ),
    ]

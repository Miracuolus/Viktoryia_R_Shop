# Generated by Django 3.0.7 on 2020-06-25 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appinfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appinfo',
            name='year',
            field=models.CharField(help_text='ГГГГ', max_length=200, verbose_name='Год разработки сайта'),
        ),
    ]

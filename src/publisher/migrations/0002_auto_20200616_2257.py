# Generated by Django 3.0.7 on 2020-06-16 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publisher',
            name='image',
            field=models.ImageField(upload_to='publishers', verbose_name='Изображение'),
        ),
    ]
# Generated by Django 3.0.7 on 2020-06-16 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0032_auto_20200616_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='photo',
            field=models.ImageField(upload_to='books', verbose_name='Изображение'),
        ),
    ]
# Generated by Django 3.0.7 on 2020-07-12 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0004_auto_20200627_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publisher',
            name='image',
            field=models.ImageField(null=True, upload_to='publishers', verbose_name='Изображение'),
        ),
    ]

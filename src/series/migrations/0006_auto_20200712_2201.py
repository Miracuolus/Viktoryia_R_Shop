# Generated by Django 3.0.7 on 2020-07-12 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0005_auto_20200712_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='image',
            field=models.ImageField(default='authors/notfound_0.png', upload_to='series', verbose_name='Изображение'),
        ),
    ]

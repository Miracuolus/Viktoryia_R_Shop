# Generated by Django 3.0.7 on 2020-06-30 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0003_auto_20200618_1114'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='series',
            options={'ordering': ['name'], 'verbose_name': 'Серия', 'verbose_name_plural': 'Серии'},
        ),
        migrations.AlterField(
            model_name='series',
            name='image',
            field=models.ImageField(upload_to='series', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='series',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='Серия'),
        ),
    ]

# Generated by Django 3.0.7 on 2020-06-27 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0044_auto_20200621_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='Название книги'),
        ),
    ]
# Generated by Django 3.0.7 on 2020-06-15 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0002_author_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='date',
            field=models.DateField(verbose_name='Дата рождения'),
        ),
    ]

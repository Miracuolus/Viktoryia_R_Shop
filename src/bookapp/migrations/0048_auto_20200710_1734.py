# Generated by Django 3.0.7 on 2020-07-10 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0047_import_book'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='import_book',
            options={'verbose_name': 'Каталог книг', 'verbose_name_plural': 'Каталоги книг'},
        ),
    ]

# Generated by Django 3.0.7 on 2020-07-17 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appinfo', '0006_import_appinfo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='import_appinfo',
            options={'verbose_name': 'Каталог информации о приложении', 'verbose_name_plural': 'Каталоги информации о приложении'},
        ),
    ]
# Generated by Django 3.0.7 on 2020-06-27 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0003_auto_20200627_1850'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publisher',
            options={'ordering': ['name'], 'verbose_name': 'Издательство', 'verbose_name_plural': 'Издательства'},
        ),
    ]
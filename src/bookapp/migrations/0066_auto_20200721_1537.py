# Generated by Django 3.0.7 on 2020-07-21 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0065_auto_20200721_1424'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment_book',
            options={'ordering': ['book'], 'verbose_name': 'Комментарий к книге', 'verbose_name_plural': 'Комментарии к книгам'},
        ),
    ]

# Generated by Django 3.0.7 on 2020-06-19 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0037_auto_20200618_1134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='user',
        ),
    ]
# Generated by Django 3.0.7 on 2020-06-19 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0040_auto_20200619_2224'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('view_active', 'Can view active books')]},
        ),
    ]
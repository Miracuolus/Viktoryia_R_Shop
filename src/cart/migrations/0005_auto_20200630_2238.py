# Generated by Django 3.0.7 on 2020-06-30 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20200630_2232'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='booktocart',
            unique_together=set(),
        ),
    ]
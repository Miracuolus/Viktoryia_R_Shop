# Generated by Django 3.0.7 on 2020-07-19 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0058_auto_20200719_1612'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='comment_book',
            unique_together=set(),
        ),
    ]

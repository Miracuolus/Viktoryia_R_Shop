# Generated by Django 3.0.7 on 2020-07-15 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0025_auto_20200715_1405'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment_order',
            old_name='comment',
            new_name='text',
        ),
    ]
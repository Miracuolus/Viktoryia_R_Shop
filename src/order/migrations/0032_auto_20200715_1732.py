# Generated by Django 3.0.7 on 2020-07-15 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0031_auto_20200715_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_order',
            name='comment',
            field=models.TextField(max_length=100, verbose_name='Комментарий'),
        ),
    ]

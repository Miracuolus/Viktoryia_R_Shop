# Generated by Django 3.0.7 on 2020-07-21 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0067_auto_20200721_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_book',
            name='comment',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Комментарий'),
        ),
    ]
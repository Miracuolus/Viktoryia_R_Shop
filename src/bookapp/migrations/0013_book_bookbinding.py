# Generated by Django 3.0.7 on 2020-06-15 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0012_book_pages'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='bookbinding',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Переплет'),
        ),
    ]
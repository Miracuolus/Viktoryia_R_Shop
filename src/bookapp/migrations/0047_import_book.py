# Generated by Django 3.0.7 on 2020-07-10 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0046_auto_20200627_1952'),
    ]

    operations = [
        migrations.CreateModel(
            name='Import_Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_books', models.FileField(upload_to='files', verbose_name='Каталог товаров')),
            ],
        ),
    ]

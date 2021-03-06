# Generated by Django 3.0.7 on 2020-07-16 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0018_auto_20200712_2201'),
    ]

    operations = [
        migrations.CreateModel(
            name='Import_Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_author', models.FileField(upload_to='files', verbose_name='Каталог авторов')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
            ],
            options={
                'verbose_name': 'Каталог авторов',
                'verbose_name_plural': 'Каталоги авторов',
            },
        ),
    ]

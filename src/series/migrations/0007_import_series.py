# Generated by Django 3.0.7 on 2020-07-16 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0006_auto_20200712_2201'),
    ]

    operations = [
        migrations.CreateModel(
            name='Import_Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_series', models.FileField(upload_to='files', verbose_name='Каталог серий')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
            ],
            options={
                'verbose_name': 'Каталог серий',
                'verbose_name_plural': 'Каталоги серий',
            },
        ),
    ]

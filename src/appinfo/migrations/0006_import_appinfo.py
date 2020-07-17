# Generated by Django 3.0.7 on 2020-07-17 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appinfo', '0005_auto_20200627_2017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Import_AppInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_info', models.FileField(upload_to='files', verbose_name='Информация о приложении')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
            ],
            options={
                'verbose_name': 'Каталог информации а приложении',
                'verbose_name_plural': 'Каталоги информации а приложении',
            },
        ),
    ]
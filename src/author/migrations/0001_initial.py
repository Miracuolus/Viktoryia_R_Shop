# Generated by Django 3.0.7 on 2020-06-15 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Автор')),
                ('description', models.TextField(blank=True, help_text='Поле может быть пустым', null=True, verbose_name='Биография')),
            ],
        ),
    ]

# Generated by Django 3.0.7 on 2020-07-24 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0019_import_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='description',
            field=models.TextField(blank=True, default='', help_text='Поле может быть пустым', null=True, verbose_name='Биография'),
        ),
    ]

# Generated by Django 3.0.7 on 2020-07-23 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0071_auto_20200721_1738'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['name'], 'permissions': [('view_active_book', 'Can view active books'), ('view_admin_db', 'Can view admin db')], 'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
    ]

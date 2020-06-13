# Generated by Django 3.0.7 on 2020-06-13 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('genre', '0001_initial'),
        ('bookapp', '0002_auto_20200605_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='genre.Genre', verbose_name='Жанр книги'),
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
    ]
# Generated by Django 3.0.7 on 2020-06-15 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0001_initial'),
        ('bookapp', '0006_book_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='series',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, to='series.Series', verbose_name='Серия'),
            preserve_default=False,
        ),
    ]

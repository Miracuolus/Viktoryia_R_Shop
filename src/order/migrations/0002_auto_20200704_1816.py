# Generated by Django 3.0.7 on 2020-07-04 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='address_1',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Адрес'),
        ),
    ]
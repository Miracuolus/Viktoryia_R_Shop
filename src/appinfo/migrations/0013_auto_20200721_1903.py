# Generated by Django 3.0.7 on 2020-07-21 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appinfo', '0012_auto_20200721_1900'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rate_currency',
            old_name='eur',
            new_name='EUR',
        ),
        migrations.RenameField(
            model_name='rate_currency',
            old_name='rub',
            new_name='RUB',
        ),
        migrations.RenameField(
            model_name='rate_currency',
            old_name='usd',
            new_name='USD',
        ),
    ]

# Generated by Django 3.0.7 on 2020-07-21 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0070_auto_20200721_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_book',
            name='rating',
            field=models.CharField(choices=[('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1'), ('0', '0')], max_length=100, null=True, verbose_name='Оценка'),
        ),
    ]

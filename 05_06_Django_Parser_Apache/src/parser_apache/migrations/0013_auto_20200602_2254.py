# Generated by Django 3.0.6 on 2020-06-02 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_apache', '0012_parser_bot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parser',
            name='bot',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Боты'),
        ),
    ]
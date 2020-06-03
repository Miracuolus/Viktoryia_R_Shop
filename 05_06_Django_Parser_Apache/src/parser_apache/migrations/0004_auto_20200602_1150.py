# Generated by Django 3.0.6 on 2020-06-02 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_apache', '0003_auto_20200602_0309'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log', models.TextField(verbose_name='Лог')),
                ('time', models.DateTimeField(verbose_name='Дата и время записи')),
                ('brouser', models.TextField(blank=True, null=True, verbose_name='Браузеры')),
            ],
        ),
        migrations.RemoveField(
            model_name='brousers',
            name='brousers',
        ),
        migrations.DeleteModel(
            name='Log',
        ),
        migrations.RemoveField(
            model_name='time_from_log',
            name='line',
        ),
        migrations.DeleteModel(
            name='Brousers',
        ),
        migrations.DeleteModel(
            name='Row_line',
        ),
        migrations.DeleteModel(
            name='Time_from_log',
        ),
    ]
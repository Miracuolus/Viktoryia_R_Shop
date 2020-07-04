# Generated by Django 3.0.7 on 2020-07-04 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_auto_20200704_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='code_phone',
            field=models.SmallIntegerField(choices=[(8029, '(029)'), (8033, '(033)'), (8044, '(044)'), (8017, '(017)')], null=True, verbose_name='Код номера'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.PositiveIntegerField(help_text='7 цифр', null=True, verbose_name='Телефон'),
        ),
    ]
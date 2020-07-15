# Generated by Django 3.0.7 on 2020-07-15 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0027_auto_20200715_1513'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment_order',
            old_name='text',
            new_name='comment',
        ),
        migrations.RemoveField(
            model_name='order',
            name='comment',
        ),
        migrations.AddField(
            model_name='comment_order',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.Order', verbose_name='Заказ'),
        ),
    ]

# Generated by Django 3.0.7 on 2020-07-07 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_auto_20200705_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('open', 'Открыт'), ('in process', 'В обработке'), ('delivery', 'Доставка'), ('cancel', 'Отменен'), ('close', 'Закрыт')], default='Открыт', max_length=100, verbose_name='Статус заказа'),
        ),
    ]

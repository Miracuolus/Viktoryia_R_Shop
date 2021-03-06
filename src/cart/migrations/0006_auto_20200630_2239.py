# Generated by Django 3.0.7 on 2020-06-30 19:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookapp', '0046_auto_20200627_1952'),
        ('cart', '0005_auto_20200630_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='carts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='booktocart',
            unique_together={('cart', 'book')},
        ),
    ]

# Generated by Django 3.0.7 on 2020-06-15 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0004_auto_20200615_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

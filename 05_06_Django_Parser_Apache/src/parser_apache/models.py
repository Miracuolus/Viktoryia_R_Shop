from django.db import models
from Parser_Apache_logs import Ratomskaya_parser_apache_logs as Parser

# Create your models here.

class Row_line(models.Model):
    name = models.CharField(
        verbose_name='Строка лога',
        max_length=400
    )

    def __str__(self):
        return self.name

class Time_from_log(models.Model):
    name = models.DateTimeField(
        verbose_name='Дата и время записи',
    )
    line = models.ForeignKey(
        Row_line,
        on_delete=models.PROTECT,
        verbose_name='Соответствующая дата',
    )
    def __str__(self):
        return self.name

class Brousers(models.Model):
    brousers = models.ForeignKey(
        Row_line,
        on_delete=models.PROTECT,
        verbose_name='Браузеры',
    )
    name = models.TextField(
        verbose_name='Браузеры',
        null=True,
        blank=True
    )
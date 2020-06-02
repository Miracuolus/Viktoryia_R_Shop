from django.db import models


# Create your models here.
class Parser(models.Model):
    log = models.TextField(
        verbose_name='Лог',
    )

    time = models.DateTimeField(
        verbose_name='Дата и время запроса',
    )
    brouser = models.CharField(
        verbose_name='Браузеры',
        max_length=300,
        null=True,
        blank=True,
    )
    bot = models.CharField(
        verbose_name='Боты',
        max_length=300,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'Строка {self.pk}'
from django.db import models


# Create your models here.
class Parser(models.Model):
    log = models.TextField(
        verbose_name='Лог',
    )
    time = models.DateTimeField(
        verbose_name='Дата и время записи',
    )
    brouser = models.TextField(
        verbose_name='Браузеры',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.time
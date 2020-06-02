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
        verbose_name='Браузер',
        max_length=300,
        null=True,
        blank=True,
    )
    bot = models.CharField(
        verbose_name='Бот',
        max_length=300,
        null=True,
        blank=True,
    )
    protocol = models.TextField(
        verbose_name='Протокол',
        null=True,
        blank=True,
    )
    referer = models.TextField(
        verbose_name='URL-запроса',
        null=True,
        blank=True,
    )
    system = models.TextField(
        verbose_name='Информация о системе',
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'Строка {self.pk}'
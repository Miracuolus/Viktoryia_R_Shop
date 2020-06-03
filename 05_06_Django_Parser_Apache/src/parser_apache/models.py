from django.db import models


# Create your models here.
class Parser(models.Model):
    log = models.TextField(
        verbose_name='Лог',
    )
    ip = models.GenericIPAddressField(
        verbose_name='IP',
        protocol='both',
        unpack_ipv4=False,
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
    status = models.IntegerField(
        verbose_name='Статус ответа сервера',
        null=True,
        blank=True,
    )
    byte = models.IntegerField(
        verbose_name='Кол-во отправленных байтов клиенту',
        null=True,
        blank=True,
    )
    referer = models.URLField(
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

class Brouser(models.Model):
    brouser = models.CharField(
        verbose_name='Браузеры',
        max_length=300,
    )
    user_agents = models.TextField(
        verbose_name='Соответ. user_agents',
        null=True,
        blank=True,
    )
    def __str__(self):
        return f'{self.brouser}'

class Bot(models.Model):
    bots = models.CharField(
        verbose_name='Бот/поисковая система',
        max_length=300,
    )
    user_agents = models.TextField(
        verbose_name='Соответ. user_agents',
        null=True,
        blank=True,
    )
    def __str__(self):
        return f'{self.bots}'
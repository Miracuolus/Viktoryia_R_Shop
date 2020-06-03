from django.db import models
from Parser_Apache_logs import Ratomskaya_parser_apache_logs as P_A #


# Create your models here.

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
    class Meta: 
        ordering = ['brouser']

    def __str__(self):
        return f'{self.brouser}'

class Bot(models.Model):
    bots = models.CharField(
        verbose_name='Бот/поисковая система',
        max_length=300,
    )
    user_agents = models.URLField(
        verbose_name='Соответ. user_agents',
        null=True,
        blank=True,
    )
    class Meta: 
        ordering = ['bots']

    def __str__(self):
        return f'{self.bots}'

class Parser(models.Model):
    log = models.TextField(
        verbose_name='Лог',
        help_text='Лог файла Apache'
    )
    ip = models.GenericIPAddressField(
        verbose_name='IP',
        protocol='both',
        unpack_ipv4=False,
        help_text='IP запроса'
    )
    time = models.DateTimeField(
        verbose_name='Дата и время запроса',
    )
    brouser = models.CharField(
        verbose_name='Браузер',
        max_length=300,
        null=True,
        blank=True,
        help_text='Поле браузера'
    )

    brou = models.ForeignKey(
        Brouser,
        on_delete=models.CASCADE,
        verbose_name = 'Браузер лога',
        null=True,
        blank=True,
    )

    bot = models.CharField(
        verbose_name='Бот',
        max_length=300,
        null=True,
        blank=True,
    )

    bо = models.ForeignKey(
        Bot,
        on_delete=models.CASCADE,
        verbose_name = 'Бот лога',
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
        help_text='Информация о системе пользователя'
    )

    def __str__(self):
        return f'Строка {self.pk}'

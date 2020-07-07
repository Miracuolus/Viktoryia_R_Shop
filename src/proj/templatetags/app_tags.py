from django import template

register = template.Library()

from appinfo.models import AppInfo
from decimal import Decimal



if AppInfo.objects.all().exists():
    pass
else:
    AppInfo.objects.create(pk=1, name='it-shop')

@register.simple_tag
def print_app_name():
    info = AppInfo.objects.get(pk=1)
    return info

@register.simple_tag
def print_app_year():
    info = AppInfo.objects.get(pk=1)
    return info.year

sum_price = 0
sum_price_order = 0
@register.simple_tag
def multiply(value1, value2):
    global sum_price
    sum_price += value1*value2
    return value1 * value2


@register.simple_tag
def sum_filter():
    global sum_price
    global sum_price_order
    sum_price_order = sum_price
    price = sum_price
    sum_price = 0
    return price

@register.simple_tag
def sum_order():
    global sum_price_order
    price = sum_price_order
    sum_price_order = 0
    return price


@register.simple_tag
def status_messages(value):
    if value == 'success':
        return f'Успех!'
    elif value == 'debug':
        return f'Отладка.'
    elif value == 'info':
        return f'Информация!'
    elif value == 'warning':
        return f'Предупреждение!'
    elif value == 'error':
        return f'Ошибка!'

@register.simple_tag
def messages_tag(value):
    if value == 'success':
        return 'success'
    elif value == 'debug':
        return 'info'
    elif value == 'info':
        return 'info'
    elif value == 'warning':
        return 'warning'
    elif value == 'error':
        return 'danger'

sum_book = 0
@register.simple_tag
def quantity_books(value):
    global sum_book
    sum_book += value
    return ''

@register.simple_tag
def quantity_zero():
    global sum_book
    r = sum_book
    sum_book = 0
    return r
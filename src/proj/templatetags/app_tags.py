from django import template

register = template.Library()
"""
from appinfo.models import AppInfo
from decimal import Decimal
import requests
from django.utils.safestring import mark_safe



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
    return info.year"""

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

@register.simple_tag
def rate_currency():
    s = requests.get('https://www.nbrb.by/api/exrates/rates?periodicity=0')
    result = s.json()
    rate = {}
    for d in result:
        if d.get('Cur_Abbreviation') == 'USD':
            rate['USD'] = d.get('Cur_OfficialRate') * d.get('Cur_Scale')
        elif d.get('Cur_Abbreviation') == 'EUR':
            rate['EUR'] = d.get('Cur_OfficialRate') * d.get('Cur_Scale')
        elif d.get('Cur_Abbreviation') == 'RUB':
            rate['RUB'] = d.get('Cur_OfficialRate') * d.get('Cur_Scale')
    return rate

@register.simple_tag
def rate(key):
    rate = rate_currency()
    value = round(rate.get(key), 2)
    return f'{ key } - {value}'

@register.filter
def quantity_cart(value):
    count = 0
    for book in value:
        if book.quantity > book.book.quantity:
            count += 1
    if count == 0:
        return True
    else:
        return False
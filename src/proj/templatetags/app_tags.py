from django import template

register = template.Library()

from appinfo.models import AppInfo, Rate_Currency
from decimal import Decimal
import requests
from django.utils.safestring import mark_safe
import datetime



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
            rate['USD'] = round(d.get('Cur_OfficialRate') * d.get('Cur_Scale'), 4)
        elif d.get('Cur_Abbreviation') == 'EUR':
            rate['EUR'] = round(d.get('Cur_OfficialRate') * d.get('Cur_Scale'), 4)
        elif d.get('Cur_Abbreviation') == 'RUB':
            rate['RUB'] = round(d.get('Cur_OfficialRate') * d.get('Cur_Scale'), 4)
    Rate_Currency.objects.create(USD = rate['USD'], EUR = rate['EUR'], RUB = rate['RUB'])

@register.simple_tag
def rate():
    rate = Rate_Currency.objects.filter(created=datetime.date.today())
    if not rate.exists():
        rate_currency()
    return rate

@register.simple_tag
def rate_usd():
    rate_usd = rate()
    return rate_usd[0].USD

@register.simple_tag
def rate_eur():
    rate_eur = rate()
    return rate_eur[0].EUR

@register.simple_tag
def rate_rub():
    rate_rub = rate()
    return rate_rub[0].RUB

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

@register.simple_tag
def stars(value):
    temp = int(value)
    html = ''
    for i in range(0, 5):
        if temp >= 1:
            html += f'<i class="fas fa-star"></i>'
        elif temp >= 0.5:
            html += f'<i class="fas fa-star-half-alt"></i>'
        temp = temp - 1
    return mark_safe(f'<font color="#FFD700" face="Arial">{html}</font>')


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

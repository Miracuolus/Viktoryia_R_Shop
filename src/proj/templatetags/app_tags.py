from django import template

register = template.Library()

from appinfo.models import AppInfo
from decimal import Decimal



if len(AppInfo.objects.all()) == 0:
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
@register.simple_tag
def multiply(value1, value2):
    global sum_price
    sum_price += value1*value2
    return value1 * value2


@register.simple_tag
def sum_filter():
    global sum_price
    price = sum_price
    sum_price = 0
    return price
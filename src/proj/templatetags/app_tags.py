from django import template

register = template.Library()

from appinfo.models import AppInfo



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

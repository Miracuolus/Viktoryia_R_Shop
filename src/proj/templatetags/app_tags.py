from django import template
from appinfo.models import AppInfo

register = template.Library()

@register.simple_tag
def print_app_name():
    info = AppInfo.objects.get(pk=1)
    return info

@register.simple_tag
def print_app_year():
    info = AppInfo.objects.get(pk=1)
    return info.year
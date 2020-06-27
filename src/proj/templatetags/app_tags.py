from django import template
from django.contrib.auth import get_user_model
User = get_user_model()

user = User.objects.all()

register = template.Library()

@register.simple_tag
def print_app_name():
    if len(user) > 1:
        from appinfo.models import AppInfo
        info = AppInfo.objects.get(pk=1)
        return info
    else:
        return f'on-line магазин'


@register.simple_tag
def print_app_year():
    if len(user) > 1:
        from appinfo.models import AppInfo
        info = AppInfo.objects.get(pk=1)
        return info.year
    else:
        return 2020

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Customer
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
User = get_user_model()

@receiver(post_save, sender=User)
def set_group(sender, instance, created, **kwargs):
    if created:
        if Group.objects.filter(name='Customers').exists():
            obj = Group.objects.get(name='Customers')
        else:
            obj, created = Group.objects.create(name='Customers',
            defaults={},
            )
        instance.groups.add(obj)
        Customer.objects.filter(user=instance).update(group = obj)
    

#post_save.connect(set_group, sender=User)
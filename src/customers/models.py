from django.db import models

from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()
class Customer(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

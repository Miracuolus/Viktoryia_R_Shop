from django import forms
from . models import BooktoCart
from django.contrib.auth.models import User

class CartForm(forms.ModelForm):
    class Meta:
        model = BooktoCart
        fields = ('book',
                  'quantity',
                  'price',
        )

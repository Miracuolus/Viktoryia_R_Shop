from django import forms
from . models import Cart
from django.contrib.auth.models import User

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ('book',
                  'quantity',
                  'price',
        )



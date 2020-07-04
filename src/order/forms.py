from django import forms
from . models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('code_phone',
                  'phone',
                  'country',
                  'city',
                  'index',
                  'address',
)
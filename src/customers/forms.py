from django import forms
from . models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('user',
                  'log',
                  'password',
                  'mail',
                  'first_name',
                  'last_name',
                  'code_phone',
                  'phone',
                  'country',
                  'city',
                  'index',
                  'address_1',
                  'address_2',
        )
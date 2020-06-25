from django import forms
from . models import AppInfo

class AppInfoForm(forms.ModelForm):
    class Meta:
        model = AppInfo
        fields = ('name',
                  'image',
                  'year',
                  'description',
                  'payment',
                  'delivery',
        )
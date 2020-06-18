from django import forms
from . models import Series

class SeriesForm(forms.ModelForm):
    class Meta:
        model = Series
        fields = ('name',
                  'image',
                  'description',
        )
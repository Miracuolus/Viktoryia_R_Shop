from django import forms
from . models import Series

class GenreForm(forms.ModelForm):
    class Meta:
        model = Series
        fields = ('name',
                  'description',
        )
from django import forms
from . models import Publisher

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ('name',
                  'image',
                  'description',
        )
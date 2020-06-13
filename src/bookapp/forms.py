from django import forms
from genre.models import Genre

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ('name',
                  'description',
        )

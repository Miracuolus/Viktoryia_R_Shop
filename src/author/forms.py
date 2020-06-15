from django import forms
from . models import Author

class GenreForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name',
                  'date',
                  'description',
        )
from django import forms
from . models import Genre, Import_Genre
import io
import csv

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ('name',
                  'description',
        )


class ImportForm(forms.ModelForm):
    file_genre = forms.FileField(
        label='Загрузка файла',
    )

    def process_file(self):
        data = io.TextIOWrapper(self.cleaned_data['file_genre'].file)
        reader = csv.DictReader(data)
        for b in reader:
            if Genre.objects.filter(name=b['name']).exists():
                genre = Genre.objects.filter(name=b['name']).update(
                    description  = b['description'],
                )
            else:
                genre, created = Genre.objects.update_or_create(
                    name = b['name'],
                    description  = b['description'],
                    defaults = {}
                )
        self.save()
        return data
        
    class Meta:
        model = Import_Genre
        fields = ('file_genre', )
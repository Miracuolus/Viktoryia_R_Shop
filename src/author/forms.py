from django import forms
from . models import Author, Import_Author
import io
import csv

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name',
                  'date',
                  'image',
                  'description',
        )

class ImportForm(forms.ModelForm):
    file_authors = forms.FileField(
        label='Загрузка файла',
    )

    def process_file(self):
        data = io.TextIOWrapper(self.cleaned_data['file_authors'].file)
        reader = csv.DictReader(data)
        for b in reader:
            if Author.objects.filter(name=b['name']).exists():
                author = Author.objects.filter(name=b['name']).update(
                    date = b['date'],
                    image = b['photo'],
                    description  = b['description'],
                )
            else:
                author, created = Author.objects.update_or_create(
                    name = b['name'],
                    date = b['date'],
                    image = b['photo'],
                    description  = b['description'],
                    defaults = {}
                )
        return data
        
    class Meta:
        model = Import_Author
        fields = ('file_authors', )
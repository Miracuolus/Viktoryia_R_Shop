from django import forms
from . models import Series, Import_Series
import io
import csv

class SeriesForm(forms.ModelForm):
    class Meta:
        model = Series
        fields = ('name',
                  'image',
                  'description',
        )

class ImportForm(forms.ModelForm):
    file_series = forms.FileField(
        label='Загрузка файла',
    )

    def process_file(self):
        data = io.TextIOWrapper(self.cleaned_data['file_series'].file)
        reader = csv.DictReader(data)
        for b in reader:
            if Series.objects.filter(name=b['name']).exists():
                series = Series.objects.filter(name=b['name']).update(
                    image = b['photo'],
                    description  = b['description'],
                )
            else:
                series, created = Series.objects.update_or_create(
                    name = b['name'],
                    image = b['photo'],
                    description  = b['description'],
                    defaults = {}
                )
        return data
        
    class Meta:
        model = Import_Series
        fields = ('file_series', )
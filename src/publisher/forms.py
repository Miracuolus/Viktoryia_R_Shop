from django import forms
from . models import Publisher, Import_Publisher
import io
import csv

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ('name',
                  'image',
                  'description',
        )


class ImportForm(forms.ModelForm):
    file_publisher = forms.FileField(
        label='Загрузка файла',
    )

    def process_file(self):
        data = io.TextIOWrapper(self.cleaned_data['file_publisher'].file)
        reader = csv.DictReader(data)
        for b in reader:
            if Publisher.objects.filter(name=b['name']).exists():
                publisher = Publisher.objects.filter(name=b['name']).update(
                    image = b['photo'],
                    description  = b['description'],
                )
            else:
                publisher, created = Publisher.objects.update_or_create(
                    name = b['name'],
                    image = b['photo'],
                    description  = b['description'],
                    defaults = {}
                )
        return data
        
    class Meta:
        model = Import_Publisher
        fields = ('file_publisher', )
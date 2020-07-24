from django import forms
from . models import AppInfo, Import_AppInfo
import io
import csv

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


class ImportForm(forms.ModelForm):
    file_appinfo = forms.FileField(
        label='Загрузка файла',
    )

    def process_file(self):
        data = io.TextIOWrapper(self.cleaned_data['file_appinfo'].file)
        reader = csv.DictReader(data)
        for b in reader:
            if AppInfo.objects.filter(pk=b['pk']).exists():
                app = AppInfo.objects.filter(pk=b['pk']).update(
                    name=b['name'],
                    image = b['image'],
                    year = b['year'],
                    description  = b['description'],
                    payment = b['payment'],
                    delivery  = b['delivery'],
                )
            else:
                app, created = AppInfo.objects.update_or_create(
                    name = b['name'],
                    image = b['image'],
                    year = b['year'],
                    description  = b['description'],
                    payment = b['payment'],
                    delivery  = b['delivery'],
                    defaults = {}
                )
        self.save()
        return data
        
    class Meta:
        model = Import_AppInfo
        fields = ('file_appinfo', )
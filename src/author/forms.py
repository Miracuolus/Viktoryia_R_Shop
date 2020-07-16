from django import forms
from . models import Author, Import_Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name',
                  'date',
                  'image',
                  'description',
        )

class ImportForm(forms.ModelForm):
    file_books = forms.FileField(
        label='Загрузка файла',
    )

    def process_file(self):
        data = io.TextIOWrapper(self.cleaned_data['file_books'].file)
        reader = csv.DictReader(data)
        for b in reader:
            if Author.objects.filter(pk=b['pk']).exists():
                author = Author.objects.filter(pk=b['pk']).update(
                    name = b['name'],
                    date = b['date'],
                    photo = b['photo'],
                    description  = b['description'],
                )
            else:
                author, created = Author.objects.update_or_create(
                    pk = b['pk'],
                    name = b['name'],
                    date = b['date'],
                    photo = b['photo'],
                    description  = b['description'],
                    defaults = {}
                )
        return data
        
    class Meta:
        model = Import_Author
        fields = ('file_books', )
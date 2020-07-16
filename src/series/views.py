from . forms import SeriesForm, ImportForm
from . models import Series, Import_Series
from django.views.generic import (
                                    TemplateView, 
                                    CreateView, 
                                    UpdateView, 
                                    ListView, 
                                    DeleteView,
                                    DetailView
                                )
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin # залогиненные пользователи
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import FormView

# Create your views here.
class CreateSeries(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Series
    form_class = SeriesForm
    template_name = 'series/create_series.html'
    
    def get_success_url(self):
        return reverse_lazy('series:list')
    
    def get_success_message(self, *args, **kwargs):
        return f'Серия {self.object} была добавлена'


class UpdateSeries(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Series
    form_class = SeriesForm
    template_name = 'series/update_series.html'
    
    def get_success_url(self):
        return reverse_lazy('series:list')
    
    def get_success_message(self, *args, **kwargs):
        return f'Серия {self.object} была изменена'

class DeleteSeries(LoginRequiredMixin, DeleteView):
    model = Series
    template_name = 'series/delete_series.html'

    def get_success_url(self):
        return reverse_lazy('series:list')


class SeriesList(LoginRequiredMixin, ListView):
    template_name = 'series/list_series.html'
    model = Series
    paginate_by = 20


class DetailSeries(DetailView):
    model = Series
    template_name = 'series/detail_series.html'

    def get_success_url(self):
        return reverse_lazy('series:detail', kwargs={'pk':self.object.pk})


class ImportSeries(LoginRequiredMixin, SuccessMessageMixin, FormView):
    form_class = ImportForm
    template_name = 'series/import_series.html'

    def get_success_url(self):    
        return reverse_lazy('series:list')
    
    def get_success_message(self, *args, **kwargs):
        return f'Каталог серий импортирован'
    
    def form_valid(self, form):
        Import_Series.objects.create(file_series = self)
        form.process_file()
        
        #file_import.save()
        return super().form_valid(form)

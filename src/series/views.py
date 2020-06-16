from . forms import SeriesForm
from . models import Series
from django.views.generic import (
                                    TemplateView, 
                                    CreateView, 
                                    UpdateView, 
                                    ListView, 
                                    DeleteView,
                                    DetailView
                                )
from django.urls import reverse_lazy

# Create your views here.
class CreateSeries(CreateView):
    model = Series
    form_class = SeriesForm
    template_name = 'series/create_series.html'
    
    def get_success_url(self):
        return reverse_lazy('series:list')


class UpdateSeries(UpdateView):
    model = Series
    form_class = SeriesForm
    template_name = 'series/update_series.html'
    
    def get_success_url(self):
        return reverse_lazy('series:list')

class DeleteSeries(DeleteView):
    model = Series
    template_name = 'series/delete_series.html'

    def get_success_url(self):
        return reverse_lazy('series:list')


class SeriesList(ListView):
    template_name = 'series/list_series.html'
    model = Series


class DetailSeries(DetailView):
    model = Series
    template_name = 'series/detail_series.html'

    def get_success_url(self):
        return reverse_lazy('series:detail', kwargs={'pk':self.object.pk})

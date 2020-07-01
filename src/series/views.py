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
from django.contrib.auth.mixins import LoginRequiredMixin # залогиненные пользователи
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
class CreateSeries(LoginRequiredMixin, CreateView):
    model = Series
    form_class = SeriesForm
    template_name = 'series/create_series.html'
    
    def get_success_url(self):
        return reverse_lazy('series:list')


class UpdateSeries(LoginRequiredMixin, UpdateView):
    model = Series
    form_class = SeriesForm
    template_name = 'series/update_series.html'
    
    def get_success_url(self):
        return reverse_lazy('series:list')

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

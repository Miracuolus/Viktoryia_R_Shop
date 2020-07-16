from . forms import PublisherForm, ImportForm
from . models import Publisher
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
class CreatePublisher(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Publisher
    form_class = PublisherForm
    template_name = 'publisher/create_publisher.html'
    
    def get_success_url(self):
        return reverse_lazy('publisher:list')
    
    def get_success_message(self, *args, **kwargs):
        return f'Издательство {self.object} было добавлено'


class UpdatePublisher(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Publisher
    form_class = PublisherForm
    template_name = 'publisher/update_publisher.html'
    
    def get_success_url(self):
        return reverse_lazy('publisher:list')
    
    def get_success_message(self, *args, **kwargs):
        return f'Издательство {self.object} было изменено'

class DeletePublisher(LoginRequiredMixin, DeleteView):
    model = Publisher
    template_name = 'publisher/delete_publisher.html'

    def get_success_url(self):
        return reverse_lazy('publisher:list')


class PublisherList(LoginRequiredMixin, ListView):
    template_name = 'publisher/list_publisher.html'
    model = Publisher
    paginate_by = 20


class DetailPublisher(DetailView):
    model = Publisher
    template_name = 'publisher/detail_publisher.html'

    def get_success_url(self):
        return reverse_lazy('publisher:detail', kwargs={'pk':self.object.pk})


class ImportPublisher(LoginRequiredMixin, SuccessMessageMixin, FormView):
    form_class = ImportForm
    template_name = 'publisher/import_publisher.html'

    def get_success_url(self):    
        return reverse_lazy('publisher:list')
    
    def get_success_message(self, *args, **kwargs):
        return f'Каталог издательств импортирован'
    
    def form_valid(self, form):
        #form.save()
        form.process_file()
        return super().form_valid(form)

from . forms import PublisherForm
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

# Create your views here.
class CreatePublisher(LoginRequiredMixin, CreateView):
    model = Publisher
    form_class = PublisherForm
    template_name = 'publisher/create_publisher.html'
    
    def get_success_url(self):
        return reverse_lazy('publisher:list')


class UpdatePublisher(LoginRequiredMixin, UpdateView):
    model = Publisher
    form_class = PublisherForm
    template_name = 'publisher/update_publisher.html'
    
    def get_success_url(self):
        return reverse_lazy('publisher:list')

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

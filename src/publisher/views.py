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

# Create your views here.
class CreatePublisher(CreateView):
    model = Publisher
    form_class = PublisherForm
    template_name = 'publisher/create_publisher.html'
    
    def get_success_url(self):
        return reverse_lazy('publisher:list')


class UpdatePublisher(UpdateView):
    model = Publisher
    form_class = PublisherForm
    template_name = 'publisher/update_publisher.html'
    
    def get_success_url(self):
        return reverse_lazy('publisher:list')

class DeletePublisher(DeleteView):
    model = Publisher
    template_name = 'publisher/delete_publisher.html'

    def get_success_url(self):
        return reverse_lazy('publisher:list')


class PublisherList(ListView):
    template_name = 'publisher/list_publisher.html'
    model = Publisher


class DetailPublisher(DetailView):
    model = Publisher
    template_name = 'publisher/detail_publisher.html'

    def get_success_url(self):
        return reverse_lazy('publisher:detail', kwargs={'pk':self.object.pk})

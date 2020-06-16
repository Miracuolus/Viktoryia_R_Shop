from . models import Author
from . forms import AuthorForm
from django.views.generic import (  TemplateView, 
                                    CreateView, 
                                    UpdateView, 
                                    ListView, 
                                    DeleteView,
                                    DetailView
                                )
from django.urls import reverse_lazy


# Create your views here.
class CreateAuthor(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author/create_author.html'
     
    def get_success_url(self):
        return reverse_lazy('author:list')

class UpdateAuthor(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author/update_author.html'
    
    def get_success_url(self):
        return reverse_lazy('author:list')

class DeleteAuthor(DeleteView):
    model = Author
    template_name = 'author/delete_author.html'
    context_object_name = 'author'

    def get_success_url(self):
        return reverse_lazy('author:list')


class AuthorList(ListView):
    template_name = 'author/list_author.html'
    model = Author
    form_class = AuthorForm


class DetailAuthor(DetailView):
    model = Author
    template_name = 'author/detail_author.html'

    def get_success_url(self):
        return reverse_lazy('author:detail', kwargs={'pk':self.object.pk})
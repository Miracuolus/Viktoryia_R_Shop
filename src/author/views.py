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
from django.contrib.auth.mixins import LoginRequiredMixin # залогиненные пользователи
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.
class CreateAuthor(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author/create_author.html'
    
    def get_success_message(self, *args, **kwargs):
        return f'Автор {self.object} был успешно добавлен'


    def get_success_url(self):
        return reverse_lazy('author:list')

class UpdateAuthor(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author/update_author.html'


    def get_success_message(self, *args, **kwargs):
        return f'Автор {self.object} была успешно изменен'


    def get_success_url(self):
        return reverse_lazy('author:list')

class DeleteAuthor(LoginRequiredMixin, DeleteView):
    model = Author
    template_name = 'author/delete_author.html'
    context_object_name = 'author'

    def get_success_url(self):
        return reverse_lazy('author:list')


class AuthorList(LoginRequiredMixin, ListView):
    template_name = 'author/list_author.html'
    model = Author
    form_class = AuthorForm
    paginate_by = 10


class DetailAuthor(DetailView):
    model = Author
    template_name = 'author/detail_author.html'

    def get_success_url(self):
        return reverse_lazy('author:detail', kwargs={'pk':self.object.pk})
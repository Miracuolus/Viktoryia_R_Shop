from . forms import GenreForm
from . models import Genre
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
class CreateGenre(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Genre
    form_class = GenreForm
    template_name = 'genre/create_genre.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['creategenre'] = GenreForm()
        return context
    
    def get_success_url(self):
        return reverse_lazy('genre:list')
    
    def get_success_message(self, *args, **kwargs):
        return f'Жанр {self.object} был добавлен'


class UpdateGenre(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Genre
    form_class = GenreForm
    template_name = 'genre/update_genre.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['updategenre'] = GenreForm(instance=Genre.objects.get(pk=self.kwargs['pk']))
        #UpdateGenre.success_url = '/update/' + str(self.kwargs['pk'])
        return context
    
    def get_success_url(self):
        return reverse_lazy('genre:list')
    
    def get_success_message(self, *args, **kwargs):
        return f'Жанр {self.object} был изменен'

class DeleteGenre(LoginRequiredMixin, DeleteView):
    model = Genre
    template_name = 'genre/delete_genre.html'
    context_object_name = 'genre'

    def get_success_url(self):
        return reverse_lazy('genre:list')


class GenreList(LoginRequiredMixin, ListView):
    template_name = 'genre/list_genre.html'
    context_object_name = 'genre_list'
    model = Genre
    paginate_by = 14


class DetailGenre(DetailView):
    model = Genre
    template_name = 'genre/detail_genre.html'

    def get_success_url(self):
        return reverse_lazy('genre:detail', kwargs={'pk':self.object.pk})

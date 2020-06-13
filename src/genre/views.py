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

# Create your views here.
class CreateGenre(CreateView):
    model = Genre
    form_class = GenreForm
    template_name = 'genre/create_genre.html'
    success_url = '/main/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['creategenre'] = GenreForm()
        return context


class UpdateGenre(UpdateView):
    model = Genre
    form_class = GenreForm
    template_name = 'genre/update_genre.html'
    #success_url = '/update/'
    success_url = '/main/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['updategenre'] = GenreForm(instance=Genre.objects.get(pk=self.kwargs['pk']))
        #UpdateGenre.success_url = '/update/' + str(self.kwargs['pk'])
        return context

class DeleteGenre(DeleteView):
    model = Genre
    template_name = 'genre/delete_genre.html'
    context_object_name = 'genre'
    success_url = '/main/'

class GenreList(ListView):
    template_name = 'genre/list_genre.html'
    context_object_name = 'genre_list'
    model = Genre


class DetailGenre(DetailView):
    model = Genre
    template_name = 'genre/index.html'
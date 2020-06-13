from . forms import GenreForm
from . models import Genre
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import ListView
from django.views.generic import DeleteView

# Create your views here.
class CreateGenre(CreateView):
    model = Genre
    form_class = GenreForm
    template_name = 'bookapp/create_genre.html'
    success_url = '/main/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['creategenre'] = GenreForm()
        return context


class UpdateGenre(UpdateView):
    model = Genre
    form_class = GenreForm
    template_name = 'bookapp/update_genre.html'
    #success_url = '/update/'
    success_url = '/main/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['updategenre'] = GenreForm(instance=Genre.objects.get(pk=self.kwargs['pk']))
        #UpdateGenre.success_url = '/update/' + str(self.kwargs['pk'])
        return context


class Test(ListView):
    template_name = 'bookapp/index.html'
    context_object_name = 'genre_list'
    model = Genre

class DeleteGenre(DeleteView):
    model = Genre
    template_name = 'bookapp/delete_genre.html'
    context_object_name = 'genre'
    success_url = '/main/'

class GenreView(ListView):
    template_name = 'bookapp/list_genre.html'
    context_object_name = 'genre_list'
    model = Genre
from . models import Genre, Book
from . forms import GenreForm
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import ListView
from django.views.generic import DeleteView


# Create your views here.
"""
class Test(TemplateView):
    template_name = 'bookapp/index.html'
    def get_context_data(self, **kwargs):
        kwargs.setdefault('view', self)
        if self.extra_context is not None:
            kwargs.update(self.extra_context)
        return kwargs
    
    def setup(self, request, *args, **kwargs):
        self.request = request
        self.args = args
        self.kwargs = kwargs

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        pk=self.kwargs['pk']
        g = Genre.objects.get(pk=self.kwargs['pk'])
        #context['testgenre'] = GenreForm(instance=Genre.objects.get(pk=self.kwargs['pk']))
        if self.request.method == 'GET':
            context['testgenre'] = GenreForm(instance=Genre.objects.get(pk=self.kwargs['pk']))
            context['t'] = 0
        elif self.request.method == 'POST':
            context['testgenre'] = GenreForm(instance=Genre.objects.get(pk=self.kwargs['pk']))
        return self.render_to_response(context)
"""

class CreateGenre(CreateView):
    model = Genre
    form_class = GenreForm
    template_name = 'bookapp/create_genre.html'
    success_url = '/listgenre/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['creategenre'] = GenreForm()
        return context


class UpdateGenre(UpdateView):
    model = Genre
    form_class = GenreForm
    template_name = 'bookapp/update_genre.html'
    success_url = '/update/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['updategenre'] = GenreForm(instance=Genre.objects.get(pk=self.kwargs['pk']))
        UpdateGenre.success_url = '/update/' + str(self.kwargs['pk'])
        return context


class GenreView(ListView):
    template_name = 'bookapp/index.html'
    context_object_name = 'genre_list'
    model = Genre

class DeleteGenre(DeleteView):
    model = Genre
    template_name = 'bookapp/delete_genre.html'
    context_object_name = 'genre'
    success_url = '/listgenre/'

#from django.shortcuts import render
#from django.http import HttpResponse
from . models import Genre, Book
from . forms import GenreForm
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.views.generic import UpdateView


# Create your views here.
class Test(TemplateView):
    template_name = 'bookapp/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

class CreateGenre(CreateView):
    model = Genre
    form_class = GenreForm
    template_name = 'bookapp/create_genre.html'
    success_url = '/create/'
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
    


"""def func_request_work(request, pk):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            #pass
            for g in Genre.objects.get(pk=pk):
                g.name = form.name
                g.description = form.description 
    elif request.method == 'GET':
        g = Genre.objects.get(pk=pk)
        #g.name = request.name
        #g.description = request.description
        form = GenreForm(g)
    return render(request, template_name='bookapp/index.html', context={'form':form})"""

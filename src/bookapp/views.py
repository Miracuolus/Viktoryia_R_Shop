from . models import Book
from . forms import BookForm
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
class CreateBook(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'bookapp/create_book.html'
     
    def get_success_url(self):
        return reverse_lazy('book:list')

class BookList(ListView):
    template_name = 'bookapp/list_book.html'
    context_object_name = 'book_list'
    model = Book
    field = ('name',
             'photo',
             'price',
             'author',
             'description',
             'quantity',
             'active',
             'user',
    )
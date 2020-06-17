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
import datetime


# Create your views here.
class CreateBook(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'bookapp/create_book.html'
     
    def get_success_url(self):
        return reverse_lazy('book:list')

class UpdateBook(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'bookapp/update_book.html'
    
    def get_success_url(self):
        return reverse_lazy('book:list')

class DeleteBook(DeleteView):
    model = Book
    template_name = 'bookapp/delete_book.html'

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

class DetailBook(DetailView):
    model = Book
    template_name = 'bookapp/detail_book.html'

    def get_success_url(self):
        return reverse_lazy('book:detail', kwargs={'pk':self.object.pk})

class ListContextBook(ListView):
    template_name = 'main.html'
    model = Book

class ListNewBook(ListView):
    template_name = 'bookapp/list_home_book.html'
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        B = Book.objects.all()
        count_b = 0
        new_book = []
        for _ in range(0, len(B)):
            count_b += 1
            for b in Book.objects.filter(pk=count_b):
                date_now = datetime.date.today()
                date_created = b.created.date()
                if date_now.year == date_created.year:
                    if date_now.month - date_created.month <= 3:
                        new_book.append(b)
        context['context'] = new_book
        return context

class ListPopularBook(ListView):
    template_name = 'bookapp/list_home_book.html'
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        B = Book.objects.all()
        count_b = 0
        popular_book = []
        for _ in range(0, len(B)):
            count_b += 1
            for b in Book.objects.filter(pk=count_b):
                if b.rating >= 9:
                    popular_book.append(b)
        context['context'] = popular_book
        return context

class ListSaleBook(ListView):
    template_name = 'bookapp/list_home_book.html'
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        B = Book.objects.all()
        count_b = 0
        sale_book = []
        for _ in range(0, len(B)):
            count_b += 1
            for b in Book.objects.filter(pk=count_b):
                if b.price <= 10:
                    sale_book.append(b)
        context['context'] = sale_book
        return context
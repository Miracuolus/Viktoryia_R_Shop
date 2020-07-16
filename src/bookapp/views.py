from . models import Book, Import_Book
from . forms import BookForm, ImportBookForm, ImportForm
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
from django.contrib.auth.mixins import LoginRequiredMixin # залогиненные пользователи
from django.core.paginator import Paginator
from django.contrib.messages.views import SuccessMessageMixin
import csv
from django.views.generic.edit import FormView

# Create your views here.
class HomePage(TemplateView):
    template_name = 'bookapp/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context

class CreateBook(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'bookapp/create_book.html'
     
    def get_success_url(self):
        return reverse_lazy('book:list')
    

    def get_success_message(self, *args, **kwargs):
        return f'Книга {self.object} была добавлена'


class UpdateBook(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'bookapp/update_book.html'
    
    def get_success_url(self):
        return reverse_lazy('book:list')
    
    def get_success_message(self, *args, **kwargs):
        return f'Информация о книге {self.object} была изменена'


class DeleteBook(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'bookapp/delete_book.html'

    def get_success_url(self):
        return reverse_lazy('book:list')

class BookList(LoginRequiredMixin, ListView):
    template_name = 'bookapp/list_book.html'
    context_object_name = 'book_list'
    model = Book
    paginate_by = 20
    field = ('name',
             'photo',
             'price',
             'author',
             'description',
             'quantity',
             'active',
    )
    

class DetailBook(DetailView):
    model = Book
    template_name = 'bookapp/detail_book.html'

    def get_success_url(self):
        return reverse_lazy('book:detail', kwargs={'pk':self.object.pk})

class ListContextBook(ListView):
    template_name = 'bookapp/list_home_book.html'
    model = Book
    paginate_by = 15

    def get_context_data(self, **kwargs):
        user = self.request.user
        user.has_perm('bookapp.view_active_book')
        context = super().get_context_data(**kwargs)
        return context
    
    def get_queryset(self):
        """
        Показывает только доступные для заказа книги
        """
        user = self.request.user
        if user.has_perm('bookapp.view_active_book') or user.is_anonymous:
            return self.model.objects.all().filter(active=True)
        else:
            return super().get_queryset()
    

class ListNewBook(ListView):
    template_name = 'bookapp/list_home_book.html'
    model = Book
    paginate_by = 15
    field = ('name',
             'photo',
             'price',
             'author',
             'short_description',
             'quantity',
             'active',
    )

    def get_queryset(self):
        user = self.request.user
        if user.has_perm('bookapp.view_active_book') or user.is_anonymous:
            return self.model.objects.all().filter(active=True).order_by('created')
        else:
            return super().get_queryset()


class ListPopularBook(ListView):
    template_name = 'bookapp/list_home_book.html'
    model = Book
    paginate_by = 15
    field = ('name',
             'photo',
             'price',
             'author',
             'short_description',
             'quantity',
             'active',
    )

    def get_queryset(self):
        user = self.request.user
        if user.has_perm('bookapp.view_active_book') or user.is_anonymous:
            return self.model.objects.all().filter(rating__gte=9).filter(active=True).order_by('rating')
        else:
            return super().get_queryset()


class ListSaleBook(ListView):
    template_name = 'bookapp/list_home_book.html'
    model = Book
    paginate_by = 15
    field = ('name',
             'photo',
             'price',
             'author',
             'short_description',
             'quantity',
             'active',
    )
    
    def get_queryset(self):
        user = self.request.user
        if user.has_perm('bookapp.view_active_book') or user.is_anonymous:
            return self.model.objects.all().filter(price__lte = 9.99).filter(active=True).order_by('price')
        else:
            return super().get_queryset()


class ImportBooks(LoginRequiredMixin, SuccessMessageMixin, FormView):
    form_class = ImportForm
    template_name = 'bookapp/import_books.html'

    def get_success_url(self):    
        return reverse_lazy('book:list')
    
    def get_success_message(self, *args, **kwargs):
        return f'Каталог книг был импортирован'
    
    def form_valid(self, form):
        form.save()
        form.process_file()
        return super().form_valid(form)


class RatePage(TemplateView):
    template_name = 'bookapp/home_page.html'

    def get_context_data(self, **kwargs):
        s = self.requests.get('https://www.nbrb.by/api/exrates/rates?periodicity=0')
        result = s.json()
        rate = {}
        for d in result:
            if d.get('Cur_Abbreviation') == 'USD':
                rate['USD'] = d.get('Cur_OfficialRate') * d.get('Cur_Scale')
            elif d.get('Cur_Abbreviation') == 'EUR':
                rate['EUR'] = d.get('Cur_OfficialRate') * d.get('Cur_Scale')
            elif d.get('Cur_Abbreviation') == 'RUB':
                rate['RUB'] = d.get('Cur_OfficialRate') * d.get('Cur_Scale')
        context = super().get_context_data(**kwargs)
        context = {'USD': rate.get('USD'), 'EUR': rate.get('EUR'), 'RUB': rate.get('RUB'), 'rate': rate}
        return context



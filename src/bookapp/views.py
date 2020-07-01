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
from django.contrib.auth.mixins import LoginRequiredMixin # залогиненные пользователи
from django.core.paginator import Paginator
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
class HomePage(TemplateView):
    template_name = 'bookapp/home_page.html'

class AdminHomePage(LoginRequiredMixin, TemplateView):
    template_name = 'bookapp/admin_home_page.html'

class CreateBook(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'bookapp/create_book.html'
     
    def get_success_url(self):
        return reverse_lazy('book:list')

class UpdateBook(LoginRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'bookapp/update_book.html'
    
    def get_success_url(self):
        return reverse_lazy('book:list')

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

    """def get_context_data(self, **kwargs):
        user = self.request.user
        if user.has_perm('bookapp.view_active_book') or user.is_anonymous:
            context = super().get_context_data(**kwargs)
            B = Book.objects.all()
            count_b = 0
            new_book = []
            for _ in range(0, len(B)):
                count_b += 1
                for b in Book.objects.filter(pk=count_b, active=True):
                    date_now = datetime.date.today()
                    date_created = b.created.date()
                    if date_now.year == date_created.year:
                        if date_now.month - date_created.month <= 3:
                            new_book.append(b)
            context['object_list'] = new_book
            return context
        else:
            return super().get_context_data(**kwargs)"""



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

    """def get_context_data(self, **kwargs):
        user = self.request.user
        if user.has_perm('bookapp.view_active_book') or user.is_anonymous:
            context = super().get_context_data(**kwargs)
            B = Book.objects.all()
            count_b = 0
            popular_book = []
            for _ in range(0, len(B)):
                count_b += 1
                for b in Book.objects.filter(pk=count_b, active=True):
                    if b.rating >= 9:
                        popular_book.append(b)
            context['object_list'] = popular_book
            return context
        else:
            return super().get_context_data(**kwargs)"""


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
    
    """def get_context_data(self, **kwargs):
        user = self.request.user
        if user.has_perm('bookapp.view_active_book') or user.is_anonymous:
            context = super().get_context_data(**kwargs)
            B = Book.objects.all()
            count_b = 0
            sale_book = []
            for _ in range(0, len(B)):
                count_b += 1
                for b in Book.objects.filter(pk=count_b, active=True):
                    if b.price <= 10:
                        sale_book.append(b)
            context['object_list'] = sale_book
            return context
        else:
            return super().get_context_data(**kwargs)"""

from . models import BooktoCart, Cart
from . forms import CartForm
from django.views.generic import (TemplateView, 
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
from bookapp.models import Book

# Create your views here.
class CreateCart(LoginRequiredMixin, CreateView):
    model = BooktoCart
    form_class = CartForm
     
    def get_success_url(self):
        return reverse_lazy('cart:detail', kwargs={'pk':self.object.pk})

class UpdateCart(LoginRequiredMixin, UpdateView):
    model = BooktoCart
    form_class = CartForm
    
    def get_success_url(self):
        return reverse_lazy('cart:detail', kwargs={'pk':self.object.pk})
    
    def get_object(self):
        user_pk = self.kwargs.get('user_pk')
        obj, created = User.objects.get_or_create(
            username = User.objects.get(pk=user_pk),
            defaults = {}
        )
        return obj

class DeleteCart(LoginRequiredMixin, DeleteView):
    model = BooktoCart

    def get_success_url(self):
        return reverse_lazy('cart:detail', kwargs={'pk':self.object.pk})

class ListCart(ListView):
    model = BooktoCart
    form_class = CartForm
    template_name = 'cart/list_cart.html'

    def get_success_url(self):
        return reverse_lazy('book:detail', kwargs={'pk':self.object.pk})
    

    """def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['updategenre'] = CartForm(instance=Cart.objects.get(pk=self.kwargs['user_pk']))
        #UpdateGenre.success_url = '/update/' + str(self.kwargs['pk'])
        return context"""


    """def get_object(self):
        user_pk = self.kwargs.get('user_pk')
        obj, created = Cart.objects.get_or_create(
            user = User.objects.get(pk=user_pk),

            defaults = {}
        )
        return obj"""
class AddBooktoCart(UpdateView):
    model = BooktoCart
    template_name = 'cart/add_cart.html'
    fields = ('quantity',)

    def get_object(self):
        cart_pk = self.request.session.get('cart_pk')
        book_pk = self.request.GET.get('book_pk')
        book = Book.objects.get(pk=book_pk)
        user = self.request.user
        cart, created = Cart.objects.get_or_create(
            pk = cart_pk,
            user = user,
            defaults = {}
        )
        if created:
            self.request.session['cart_pk'] = cart.pk
        obj, created = self.model.objects.get_or_create(
            cart = cart,
            book = book,
            defaults = {}
        )
        return obj

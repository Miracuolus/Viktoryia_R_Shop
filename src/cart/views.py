from . models import BooktoCart, Cart
from . forms import CartForm
from django.shortcuts import redirect
from django.views.generic import (TemplateView, 
                                  CreateView, 
                                  UpdateView, 
                                  ListView, 
                                  DeleteView,
                                  DetailView
)
from django.urls import reverse_lazy, reverse
import datetime
from django.contrib.auth.mixins import LoginRequiredMixin # залогиненные пользователи
from django.core.paginator import Paginator
from bookapp.models import Book
from decimal import Decimal
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
class UpdateBookCart(UpdateView):
    model = BooktoCart
    template_name = 'cart/add_cart.html'
    fields = ('quantity',)
    
    def get_success_url(self):    
        return reverse_lazy('cart:list')
    
    def get_object(self):
        book_pk = self.request.GET.get('book_pk')
        cart_pk = self.request.session.get('cart_pk')
        book = Book.objects.get(pk=book_pk)
        user = self.request.user
        if user.is_authenticated:
            cart, created = Cart.objects.get_or_create(
                pk = cart_pk,
                user = user,
                defaults = {}
            )
        else:
            cart, created = Cart.objects.get_or_create(
                pk = cart_pk,
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

class DeleteBookCart(UpdateView):
    model = BooktoCart
    form_class = CartForm
    template_name = 'cart/list_cart.html'

    def get_success_url(self):    
        return reverse('cart:list')

    def get_object(self):
        book_pk = self.request.GET.get('book_pk')
        cart_pk = self.request.session.get('cart_pk')
        book = Book.objects.get(pk=book_pk)
        #book.delete()
        user = self.request.user
        if user.is_authenticated:
            cart, created = Cart.objects.get_or_create(
                pk = cart_pk,
                user = user,
                defaults = {}
            )
        else:
            cart, created = Cart.objects.get_or_create(
                pk = cart_pk,
                defaults = {}
            )
        if created:
            self.request.session['cart_pk'] = cart.pk
        obj = self.model.objects.get(cart = cart, book = book)
        obj.delete()
        return obj


class DeleteCart(ListView):
    model = BooktoCart
    form_class = CartForm
    template_name = 'cart/list_cart.html'

    def get_success_url(self):    
        return reverse_lazy('cart:list')

    def get_queryset(self):
        self.request.session.flush()
        self.request.session.pop('cart_pk')
        return super().get_queryset()

class ListCart(ListView):
    model = BooktoCart
    form_class = CartForm
    template_name = 'cart/list_cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_pk = self.request.session.get('cart_pk')
        user = self.request.user
        if user.is_authenticated:
            cart = Cart.objects.filter(pk=cart_pk, user=user)
        else:
            cart = Cart.objects.filter(pk=cart_pk)
        if cart:
            book_in_cart = self.model.objects.all().filter(cart=cart[0])
            context['object_list'] = book_in_cart
            return context


    def get_success_url(self):    
        return reverse_lazy('cart:list')

class AddBooktoCart(UpdateView):
    model = BooktoCart
    #template_name = 'cart/add_cart.html'
    #fields = ('quantity',)
    form_class = CartForm
    template_name = 'cart/list_cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_pk = self.request.session.get('cart_pk')
        user = self.request.user
        if user.is_authenticated:
            cart = Cart.objects.filter(pk=cart_pk, user=user)
        else:
            cart = Cart.objects.filter(pk=cart_pk)
        if cart:
            book_in_cart = self.model.objects.all().filter(cart=cart[0])
            context['object_list'] = book_in_cart
            return context

    def get_success_url(self):
        return reverse_lazy('cart:list')

    def get_object(self):
        book_pk = self.request.GET.get('book_pk')
        cart_pk = self.request.session.get('cart_pk')
        book = Book.objects.get(pk=book_pk)
        user = self.request.user
        if user.is_authenticated:
            cart, created = Cart.objects.get_or_create(
                pk = cart_pk,
                user = user,
                defaults = {}
            )
        else:
            cart, created = Cart.objects.get_or_create(
                pk = cart_pk,
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

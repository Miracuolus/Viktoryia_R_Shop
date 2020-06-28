from . models import Cart
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

# Create your views here.
class CreateCart(LoginRequiredMixin, CreateView):
    model = Cart
    form_class = CartForm
     
    def get_success_url(self):
        return reverse_lazy('cart:detail', kwargs={'pk':self.object.pk})

class UpdateCart(LoginRequiredMixin, UpdateView):
    model = Cart
    form_class = CartForm
    
    def get_success_url(self):
        return reverse_lazy('cart:detail', kwargs={'pk':self.object.pk})

class DeleteCart(LoginRequiredMixin, DeleteView):
    model = Cart

    def get_success_url(self):
        return reverse_lazy('cart:detail', kwargs={'pk':self.object.pk})

class DetailCart(DetailView):
    model = Cart

    def get_success_url(self):
        return reverse_lazy('book:detail', kwargs={'pk':self.object.pk})

from . models import Order
from . forms import OrderForm
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
from cart.models import Cart, BooktoCart
from customers.models import Customer
from decimal import Decimal
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
class UpdateOrder(SuccessMessageMixin, UpdateView):
    model = Order
    template_name = 'order/order_update.html'
    #fields = ('price',)
    form_class = OrderForm
    
    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:   
            return reverse_lazy('order:detail', kwargs={'pk':self.object.pk})
        else:
            self.request.session.flush()
            return reverse_lazy('main')

    def get_success_message(self, *args, **kwargs):
        return 'Заказ оформлен'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        cart_pk = self.request.session.get('cart_pk')
        if user.is_authenticated:
            cart = Cart.objects.filter(pk = cart_pk, user=user)
        else:
            cart = Cart.objects.filter(pk = cart_pk)
        context['cart'] = BooktoCart.objects.all().filter(cart = cart[0])
        return context

    def get_object(self):
        price = self.request.GET.get('price')
        cart_pk = self.request.session.get('cart_pk')
        user = self.request.user
        if user.is_authenticated:
            cart = Cart.objects.filter(pk = cart_pk, user=user)
            customer = Customer.objects.filter(user=user)
            obj, created = self.model.objects.get_or_create(
                cart = cart[0],
                user = user,
                price = price,
                defaults = {'code_phone': customer[0].code_phone,
                            'phone': customer[0].phone,
                            'country': customer[0].country,
                            'city': customer[0].city,
                            'index': customer[0].index,
                            'address': customer[0].address_1,
                }
            )
        else:
            cart = Cart.objects.filter(pk = cart_pk)
            obj, created = self.model.objects.get_or_create(
                cart = cart[0],
                price = price,
                defaults = {}
            )
        return obj



class DetailOrder(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'order/order_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if Order.objects.filter(pk = self.object.pk, status = 'Открыт'):
            order = Order.objects.filter(pk = self.object.pk).update(status = 'В обработке')
        user = self.request.user
        if self.request.session.get('cart_pk'):
            cart_pk = self.request.session.pop('cart_pk')
        #cart = Cart.objects.filter(pk = cart_pk, user=user)
        #context['cart'] = BooktoCart.objects.all().filter(cart = cart[0])
        return context


class OrderList(LoginRequiredMixin, ListView):
    template_name = 'order/order_list.html'
    model = Order
    paginate_by = 6
    form_class = OrderForm

class DeleteOrder(LoginRequiredMixin, UpdateView):
    model = Order
    form_class = OrderForm
              
    template_name = 'order/order_delete.html'
    
    def get_success_url(self):
        return reverse_lazy('order:detail', kwargs={'pk':self.object.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = Order.objects.filter(pk = self.object.pk).update(status = 'Отменен')
        return context
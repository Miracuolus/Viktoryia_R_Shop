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
    template_name = 'order/order_detail.html'
    #fields = ('price',)
    form_class = OrderForm
    
    def get_success_url(self):    
        return reverse_lazy('order:detail')

    def get_success_message(self, *args, **kwargs):
        return 'Заказ оформлен'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        cart_pk = self.request.session.get('cart_pk')
        cart = Cart.objects.filter(pk = cart_pk, user=user)
        context['cart'] = BooktoCart.objects.all().filter(cart = cart[0])
        return context

    def get_object(self):
        price = self.request.GET.get('price')
        cart_pk = self.request.session.get('cart_pk')
        user = self.request.user
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
                        'status': 'in process',
            }
        )
        return obj

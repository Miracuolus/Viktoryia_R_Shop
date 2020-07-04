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
from cart.models import Cart
from decimal import Decimal
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
class UpdateOrder(UpdateView):
    model = Order
    template_name = 'order/order_detail.html'
    fields = ('price',
              
    )
    
    def get_success_url(self):    
        return reverse_lazy('order:detail')
    
    def get_object(self):
        price = self.request.GET.get('price')
        cart_pk = self.request.session.get('cart_pk')
        user = self.request.user
        cart = Cart.objects.filter(pk = cart_pk, user=user)
        #self.request.session['cart_pk'] = cart.pk
        obj, created = self.model.objects.get_or_create(
            cart = cart[0],
            user = user,
            price = price,
            defaults = {}
        )
        return obj

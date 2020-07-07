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
from bookapp.models import Book
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail

# Create your views here.
class UpdateOrder_continue(SuccessMessageMixin, UpdateView):
    model = Order
    template_name = 'order/order_update.html'
    form_class = OrderForm
    

    def get_success_url(self):
        user = self.request.user
        #if Order.objects.filter(pk = self.object.pk, status = 'Открыт'):
        #    order = Order.objects.filter(pk = self.object.pk).update(status = 'В обработке')
        if user.is_authenticated:
            return reverse_lazy('order:detail', kwargs={'pk':self.object.pk})
        else:
            self.request.session.flush()
            return reverse_lazy('main')

    def get_success_message(self, *args, **kwargs):
        return 'Заказ оформлен'


class UpdateOrder_continue_admin(SuccessMessageMixin, UpdateView):
    model = Order
    template_name = 'order/order_update.html'
    fields = ('status',
              'code_phone',
              'phone',
              'country',
              'city',
              'index',
              'address',
)

    def get_success_url(self):
        return reverse_lazy('main_admin')

    def get_success_message(self, *args, **kwargs):
        return 'Статус заказа изменен'


class UpdateOrder(SuccessMessageMixin, UpdateView):
    model = Order
    template_name = 'order/order_update.html'
    form_class = OrderForm
    
    
    def get_success_url(self):
        user = self.request.user
        cart_pk = self.request.session.get('cart_pk')
        cart = Cart.objects.filter(pk = cart_pk)
        book = BooktoCart.objects.all().filter(cart = cart[0])
        for b in book:
            bb = Book.objects.filter(pk = b.book.pk)
            bb.update(quantity = (b.book.quantity - b.quantity))
            if bb[0].quantity == 0:
                Book.objects.filter(pk = b.book.pk).update(active = False)
        if Order.objects.filter(pk = self.object.pk, status = 'Открыт'):
            order = Order.objects.filter(pk = self.object.pk).update(status = 'В обработке')
            send_mail(f'Заказ №{self.object.pk}', f'Сформирован новый заказ от пользователя {user}', 'from@gmail.com',
                ['to@gmail.com'], fail_silently=False)
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
        #price = self.request.GET.get('price')
        price = 0
        cart_pk = self.request.session.get('cart_pk')
        user = self.request.user
        cart = Cart.objects.filter(pk = cart_pk)
        book = BooktoCart.objects.all().filter(cart = cart[0])
        for b in book:
            if b.quantity > b.book.quantity:
                BooktoCart.objects.filter(cart = cart[0], book = b.book.pk).update(quantity = b.book.quantity)
                price += b.book.price * b.book.quantity
            else:
                price += b.book.price * b.quantity
        if user.is_authenticated:
            cart = Cart.objects.filter(pk = cart_pk, user=user)
            customer = Customer.objects.filter(user=user)
            if self.model.objects.filter(cart = cart[0], user = user).exists():
                obj = self.model.objects.get(cart = cart[0], user = user)
                obj.price = price
            else:
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
        
        user = self.request.user
        if self.request.session.get('cart_pk'):
            cart_pk = self.request.session.pop('cart_pk')
        order = Order.objects.all().filter(pk = self.object.pk)
        cart = order[0].cart
        books = BooktoCart.objects.all().filter(cart=cart)
        context['cart'] = books
        return context


class OrderList(LoginRequiredMixin, ListView):
    template_name = 'order/order_list.html'
    model = Order
    paginate_by = 6
    form_class = OrderForm

    def get_queryset(self):
        user = self.request.user
        return self.model.objects.all().filter(user = user)


class OrderListAdmin(LoginRequiredMixin, SuccessMessageMixin, ListView):
    template_name = 'order/order_list_admin.html'
    model = Order
    paginate_by = 20
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
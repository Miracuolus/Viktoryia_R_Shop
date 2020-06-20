from . models import Customer
from . forms import CustomerForm
from django.views.generic import (
                                    TemplateView, 
                                    CreateView, 
                                    UpdateView, 
                                    ListView, 
                                    DeleteView,
                                    DetailView
                                )
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin # залогиненные пользователи
from django.contrib.auth import get_user_model
User = get_user_model()

class CreateCustomer(LoginRequiredMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer/create_customer.html'
     
    def get_success_url(self):
        return reverse_lazy('customer:list')

class CustomerList(LoginRequiredMixin, ListView):
    template_name = 'customer/list_customer.html'
    model = Customer
    form_class = CustomerForm

class UpdateCustomer(LoginRequiredMixin, UpdateView):
    model = Customer
    fields = ('user',)
    template_name = 'customer/update_customer.html'
    
    def get_object(self):
        user_pk = self.kwargs.get('user_pk')
        obj, created = self.model.objects.get_or_create(
            user = User.objects.get(pk=user_pk),
            defaults = {}
        )
        return obj
    
    def get_success_url(self):
        return reverse_lazy('customer:list')

class DeleteCustomer(LoginRequiredMixin, DeleteView):
    model = Customer
    template_name = 'customer/delete_customer.html'

    def get_success_url(self):
        return reverse_lazy('customer:list')

class DetailCustomer(DetailView):
    model = Customer
    template_name = 'customer/detail_customer.html'

    def get_success_url(self):
        return reverse_lazy('customer:detail', kwargs={'pk':self.object.pk})

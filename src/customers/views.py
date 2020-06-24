from . models import Customer
from . forms import CustomerForm, LogInForm
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
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
User = get_user_model()

class SignIn(LoginView):
    template_name = 'customer/sign_in.html'

class LogIn(FormView):
    template_name = 'customer/log_in.html'
    form_class = LogInForm
    def get_success_url(self):
        return reverse_lazy('main')

    def form_valid(self, form):
        new_user = form.save()
        group = new_user.groups.add(Group.objects.get(name='manager'))
        username = self.request.POST['username']
        password = self.request.POST['password2']
        email = self.request.POST['email']
        code_type = self.request.POST['code_type']
        phone = self.request.POST['phone']
        Customer.objects.create(user=new_user, code_phone=code_type, phone=phone, group=group)
        new_user = authenticate(self.request,username=username,password=password)
        if new_user is not None:
             if new_user.is_active:
                 login(self.request, new_user)
        return super(LogIn, self).form_valid(form)

    def form_invalid(self, form):
        return super(LogIn, self).form_invalid(form)
    

class LogOut(LogoutView):
    template_name = 'customer/log_out.html'

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
    fields = ('code_phone',
              'phone',
              'country',
              'city',
              'index',
              'address_1',
              'address_2',
        )
    template_name = 'customer/update_customer.html'
    
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

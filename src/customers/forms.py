from django import forms
from . models import Customer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('user',
                  'log',
                  'password',
                  'mail',
                  'first_name',
                  'last_name',
                  'code_phone',
                  'phone',
                  'country',
                  'city',
                  'index',
                  'address_1',
                  'address_2',
        )
class LogInForm(UserCreationForm):
    username = forms.CharField(
        label='Имя пользователя',
        max_length=100, 
    )
    email = forms.EmailField(
        max_length=200, 
        label='E-mail'
    )
    password1 = forms.CharField(
        label='Пароль',
        max_length=100,
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        max_length=100,
        widget=forms.PasswordInput(),
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
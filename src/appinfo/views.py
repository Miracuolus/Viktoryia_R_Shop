from . models import AppInfo
from . forms import AppInfoForm
from django.views.generic import (  TemplateView, 
                                    UpdateView, 
                                    DetailView
                                )
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin # залогиненные пользователи
from django.contrib.messages.views import SuccessMessageMixin


class UpdateAppInfo(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = AppInfo
    form_class = AppInfoForm
    template_name = 'appinfo/update_info.html'


    def get_success_message(self, *args, **kwargs):
        return f'Информация о приложении {self.object} была успешно изменена'


    def get_success_url(self):
        return reverse_lazy('appinfo:detail', kwargs={'pk':self.object.pk})


class DetailAppInfo(DetailView):
    model = AppInfo
    template_name = 'appinfo/detail_info.html'

    def get_success_url(self):
        return reverse_lazy('appinfo:detail', kwargs={'pk':self.object.pk})

class DetailAppInfoPayment(DetailView):
    model = AppInfo
    template_name = 'appinfo/detail_info_payment.html'

    def get_success_url(self):
        return reverse_lazy('appinfo:detail', kwargs={'pk':self.object.pk})

class DetailAppInfoDelivery(DetailView):
    model = AppInfo
    template_name = 'appinfo/detail_info_delivery.html'

    def get_success_url(self):
        return reverse_lazy('appinfo:detail', kwargs={'pk':self.object.pk})
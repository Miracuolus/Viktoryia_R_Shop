from . models import AppInfo
from . forms import AppInfoForm
from django.views.generic import (  TemplateView, 
                                    UpdateView, 
                                    DetailView
                                )
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin # залогиненные пользователи

class UpdateAppInfo(LoginRequiredMixin, UpdateView):
    model = AppInfo
    form_class = AppInfoForm
    template_name = 'appinfo/update_info.html'
    
    def get_success_url(self):
        return reverse_lazy('appinfo:detail')


class DetailAppInfo(DetailView):
    model = AppInfo
    template_name = 'appinfo/detail_info.html'

    def get_success_url(self):
        return reverse_lazy('appinfo:detail')
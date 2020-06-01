from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def parser_apache(request):
    context = {}
    return render(request, template_name='parser_apache/index.html', context=context)

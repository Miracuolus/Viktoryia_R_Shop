from django.shortcuts import render
#from Parser_Apache_logs import Ratomskaya_parser_apache_logs as Parser
from . models import Parser



# Create your views here.

def parser_apache(request):
    with open('apache_logs/apache_logs_small.txt', 'r') as fp:
        count = 0
        for line in fp.readlines():
            count += 1
            #l = Row_line.objects.create(pk=count,name=line)
            #l.save()
    context = {'count':count, 'line':line}
    
    return render(request, template_name='parser_apache/index.html', context=context)



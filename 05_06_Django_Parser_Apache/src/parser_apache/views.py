from django.shortcuts import render
from Parser_Apache_logs import Ratomskaya_parser_apache_logs as P_A
#import Time_for_Parser
from . models import Parser



# Create your views here.

def parser_apache(request):
    
    P_A.main(debug_msg=False, debug_save=False)
    with open('apache_logs/apache_logs_small.txt', 'r') as fp:
        count = 0
      
        for line in fp.readlines():
            count += 1
            #l = Parser.objects.create(pk=count,log=line,brouser=P_A.k_key.get(count))
            #l.save()
    context = {'count':count, 'line': P_A.list_time}
    
    return render(request, template_name='parser_apache/index.html', context=context)



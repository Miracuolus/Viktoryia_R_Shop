from django.shortcuts import render
from Parser_Apache_logs import Ratomskaya_parser_apache_logs as P_A
import Time_for_Parser
from . models import Parser
from datetime import datetime



# Create your views here.

def parser_apache(request):
    
    #P_A.main(debug_msg=False, debug_save=False)
    t = Time_for_Parser.main(save_logs=False)
    l_date = []
    for i in range(0, len(t)):
        r_datetime = t[i][:19]
        date = datetime.strptime(r_datetime, '%Y-%m-%d %H:%M:%S')
        l_date.append(date)
    with open('apache_logs/apache_logs_small.txt', 'r') as fp:
        count = 0
      
        for line in fp.readlines():
            count += 1
            l = Parser.objects.create(pk=count,log=line,brouser=P_A.k_key.get(count), time=l_date[count-1])
            l.save()
    context = {'count':count, 'line': l_date}
    
    return render(request, template_name='parser_apache/index.html', context=context)



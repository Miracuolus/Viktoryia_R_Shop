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
    
    count = 0
    for _ in range(0, P_A.all_request_count):
        count += 1
            #l = Parser.objects.create(pk=count,log=line,brouser=P_A.k_key.get(count), time=l_date[count-1]) # создание БД
            #l.save()
        for p in Parser.objects.filter(pk=count): # изменение БД
            p.bot = P_A.b_bot.get(count) # изменение БД
            p.save()
        
    context = {'count':count, 'line': P_A.all_request_count}
    
    return render(request, template_name='parser_apache/index.html', context=context)



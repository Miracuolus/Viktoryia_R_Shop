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
            #l.save() # создание БД
        for p in Parser.objects.filter(pk=count): # изменение БД
            #p.ip = P_A.ip_address[count-1]
            end_list_protocol = P_A.list_protocol[count-1].split('"')
            #p.protocol = end_list_protocol[0]
            e_list_protocol = end_list_protocol[1].split(' ')
            if e_list_protocol[1] != '-':
                p.status = e_list_protocol[1]
            if e_list_protocol[2] != '-':
                p.byte = e_list_protocol[2]
            ##p.bot = P_A.b_bot.get(count) # изменение БД
            ##p.referer = P_A.r_ref.get(count) # изменение БД
            p.save() # создание БД
            
        
    context = {'count':count, 'line': len(P_A.ip_address)}
    
    return render(request, template_name='parser_apache/index.html', context=context)



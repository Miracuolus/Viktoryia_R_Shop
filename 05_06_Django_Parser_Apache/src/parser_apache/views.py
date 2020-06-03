from django.shortcuts import render
from Parser_Apache_logs import Ratomskaya_parser_apache_logs as P_A
import Time_for_Parser
from . models import Parser, Brouser, Bot
from datetime import datetime

b_count = 0 
k_b = []
v_b = []
format_v_b = []
# Create your views here.


def parser_brousers(dict_brousers):
    for key, value in dict_brousers.items():
        k_b.append(key)
        v_b.append(value)


def create_bd_brousers(dict_brousers):
    global b_count
    for i in range(0, len(dict_brousers)):
        b_count += 1
        if dict_brousers == P_A.mobile_brousers:
            j = i + len(P_A.brousers)
            b = Brouser.objects.create(pk=b_count,brouser=k_b[j], user_agents=v_b[j]) # создание БД
        else:
            b = Brouser.objects.create(pk=b_count,brouser=k_b[i], user_agents=v_b[i]) # создание БД
        b.save()


def update_bd_brousers(b_count=17):
    for i in range(0, len(v_b)):
        r_b = ', '.join(v_b[i])
        format_v_b.append(r_b)

    for i in range(0, b_count):
        i += 1
        for b in Brouser.objects.filter(pk=i): # изменение БД
            print(i)
            b.user_agents = format_v_b[i-1] # изменение списка агентов
            b.save()

def create_bd_bots(dict_bots):
    global b_count
    for i in range(0, len(dict_bots)):
        b_count += 1
        if dict_bots == P_A.bots:
            j = i + len(P_A.search_systems)
            b = Bot.objects.create(pk=b_count,bots=k_b[j], user_agents=v_b[j]) # создание БД
        else:
            b = Bot.objects.create(pk=b_count,bots=k_b[i], user_agents=v_b[i]) # создание БД
        b.save()

def update_bd_bots(b_count=11):
    for i in range(0, b_count):
        i += 1
        for b in Bot.objects.filter(pk=i): # изменение БД
            print(i)
            b.user_agents = v_b[i-1] # изменение списка агентов
            b.save()


def brousers():
    global b_count
    b_count = 0  
    parser_brousers(P_A.brousers)
    parser_brousers(P_A.mobile_brousers)
    create_bd_brousers(P_A.brousers)
    create_bd_brousers(P_A.mobile_brousers)


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
            ##p.ip = P_A.ip_address[count-1]
            ##end_list_protocol = P_A.list_protocol[count-1].split('"')
            #p.protocol = end_list_protocol[0]
            ##e_list_protocol = end_list_protocol[1].split(' ')
            ##if e_list_protocol[1] != '-':
            ##    p.status = e_list_protocol[1]
            ##if e_list_protocol[2] != '-':
            ##    p.byte = e_list_protocol[2]
            ##p.bot = P_A.b_bot.get(count) # изменение БД
            ##p.referer = P_A.r_ref.get(count) # изменение БД
            ##p.save() # создание БД
            pass
    #brousers() # создание БД браузеры
    #parser_brousers(P_A.brousers)
    #parser_brousers(P_A.mobile_brousers)
    #update_bd_brousers(b_count=17)

    parser_brousers(P_A.search_systems)
    parser_brousers(P_A.bots)
    #create_bd_bots(P_A.search_systems)
    #create_bd_bots(P_A.bots)
    update_bd_bots()
        
    context = {'count': b_count, 'line': len(format_v_b)}
    
    return render(request, template_name='parser_apache/index.html', context=context)



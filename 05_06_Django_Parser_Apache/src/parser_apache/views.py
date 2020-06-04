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
def create_bd_parser(count):
    l = Parser.objects.create(pk=count, log=line, brouser=P_A.k_key.get(count), time=l_date[count-1]) # создание БД
    l.save() # создание БД


def update_bd_parser_ip(model, count):
    """
    Обновление IP
    """
    model.ip = P_A.ip_address[count-1]
    model.save()


def update_bd_parser_protocols(model, count):
    """
    Обновление протокола, статуса ответа сервера, кол-во байт
    """
    end_list_protocol = P_A.list_protocol[count-1].split('"')
    model.protocol = end_list_protocol[0]
    e_list_protocol = end_list_protocol[1].split(' ')
    if e_list_protocol[1] != '-':
        model.status = e_list_protocol[1]
    if e_list_protocol[2] != '-':
        model.byte = e_list_protocol[2]
    p.save()


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

l_date = []


def d_time(t):
    for i in range(0, len(t)):
        r_datetime = t[i][:19]
        date = datetime.strptime(r_datetime, '%Y-%m-%d %H:%M:%S')
        l_date.append(date)


def get_all(model):
    return model.objects.all()


def front_brausers(brousers):
    B = get_all(Brouser)
    count_b_user = 0
    for _ in range(0, len(B)):
        count_b_user += 1
        for b in Brouser.objects.filter(pk=count_b_user): # изменение БД
            bb = b.user_agents.split(',')
            brousers[b.brouser] = bb
    return brousers

def front_bots(bots):
    B = get_all(Bot)
    count_b_user = 0
    for _ in range(0, len(B)):
        count_b_user += 1
        for b in Bot.objects.filter(pk=count_b_user): # изменение БД
            #bb = b.user_agents.split(',')
            bots[b.bots] = b.user_agents
    return bots

def front_path(model, part):
    pat = []
    B = get_all(model)
    count_b_user = 0
    for _ in range(0, len(B)):
        count_b_user += 1
        for b in model.objects.filter(pk=count_b_user):
            list_path = {'protocol': b.protocol, 'status': b.status, 'byte': b.byte, 'referer': b.referer, 'system':b.system}
            for key, value in list_path.items():
                if key == part:
                    if value != None:
                        pat.append(value)
    return pat

def parser_apache(request):
    #P_A.main(debug_msg=False, debug_save=False) # парсер
    #t = Time_for_Parser.main(save_logs=False) # парсер
    #d_time(t) # форматирование даты/времени
    count = 0
    brousers = {}
    bots = {}
    ip = set()
    tim = set()
    all_brauser = {}
    all_bot = {}

    c_brouser = Brouser.objects.all()
    c = 0
    for _ in range(0, len(c_brouser)):
        c += 1
        for b in Brouser.objects.filter(pk=c):
            all_brauser[b.brouser] = 0
    L = get_all(Parser)
    count_all = len(L)

    for p in Parser.objects.all():
        for i in Brouser.objects.filter(brouser = p.brou):
            all_brauser[i.brouser] = all_brauser.get(i.brouser, 0) + 1
            break
    
    for p in Parser.objects.all():
        for j in Bot.objects.filter(bots = p.bо):
            all_bot[j.bots] = all_bot.get(j.bots, 0) + 1
            break

    for _ in range(0, count_all):
        count += 1
        #create_bd_parser(count) # создание БД
        for p in Parser.objects.filter(pk=count): # изменение БД
            #c = 0
            #for _ in range(0, len(c_brouser)):
            #    c += 1
                #for b in Brouser.objects.filter(pk=c):
                #    if b.brouser != None:
                #        deb.append(b.brouser)
                        #all_ip[b.brouser] = all_ip.get(b.brouser) + 1
                #    break
            ip.add(p.ip)
            tt = str(p.time)
            tt = tt[0: 10].split(' ')
            tim.add(tt[0])
            #for b in Brouser.objects.filter(brouser=p.brouser): # FK_brouser
            #    p.brou = b #P_A.k_key.get(count)
            #for b in Bot.objects.filter(bots=p.bot): # FK_bot
                #p.bо = b #P_A.k_key.get(count)
                #p.bо = Bot.bots(P_A.b_bot.get(count)) # изменение БД
            #p.save() # создание БД
    
    brousers = front_brausers(brousers) # список браузеров и user_agents из БД
    bots = front_bots(bots) # список ботов и user_agents из БД
    protocol = front_path(Parser, 'protocol')
    status = front_path(Parser, 'status')
    byte = front_path(Parser, 'byte')
    unic_satus = set()
    for i in range(0, len(status)):
        unic_satus.add(status[i])
    referer = front_path(Parser, 'referer')
    system = front_path(Parser, 'system')
    
    context = {'count': count_all,
               'ip': ip,
               'count_brousers': len(get_all(Brouser)),
               'time': tim,
               'brousers': brousers,
               'c_brousers': all_brauser,
               'bots': bots,
               'c_bots': all_bot,
               'protocol': protocol,
               'status': status,
               'unic_status': unic_satus, 
               'byte': byte,
               'referer': referer,
               'system': system,
    }
    return render(request, template_name='parser_apache/index.html', context=context)



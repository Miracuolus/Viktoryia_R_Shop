import re
import os
import collections


f = 'apache_logs.txt'
script_path = os.path.dirname(__file__)
path_file_apache = os.path.join(script_path, '..\\apache_logs\\' + f)

folder_apache_logs = os.path.abspath(path_file_apache)

brousers = {'Mozilla Firefox': ['Gecko', 'Firefox'],
            'Mozilla Firefox2': ['Gecko', 'BonEcho'],
            'Mozilla for Linux': ['Gecko', 'Firefox', 'Iceweasel'],
            'Google Chrome': ['Chrome', 'Safari'],
            'Apple Safari': ['Version', 'Safari'],
            'Opera 19': ['Chrome', 'Safari', 'OPR'],
            'Opera 12': ['Presto', 'Version'],
            'Internet Explorer': ['like', 'Gecko'],
            'Microsoft Edge': ['Chrome', 'Safari', 'Edge'],
            'Bing': ['BingPreview'],
            'Chromium': ['Ubuntu', 'Chromium', 'Chrome', 'Safari']}

mobile_brousers = {'Safari on iPhone': ['(iPhone', 'Version', 'Mobile', 'Safari'],
                   'Chrome on iPhone': ['(iPhone', 'CriOS', 'Mobile', 'Safari'],
                   'Chrome on Android': ['Android', 'Chrome', 'Mobile', 'Safari'],
                   'Others on Android': ['Android', 'Version', 'Mobile', 'Safari'],
                   'Safari on iPad': ['(iPad', 'Version', 'Mobile', 'Safari'],
                   'Chrome on iPad': ['(iPad', 'CriOS', 'Mobile', 'Safari']}

search_systems = {'Яндекс': 'http://yandex.com/bots',
                  'Google': 'http://www.google.com/bot.html',
                  'Bing': 'http://www.bing.com/bingbot.htm',
                  'Yahoo! Slurp': 'http://help.yahoo.com/help/us/ysearch/slurp',
                  'Mail.ru': 'http://go.mail.ru/help/robots'}

bots = {'Ahrefs': 'http://ahrefs.com/robot/',
        'Majestic': 'http://www.majestic12.co.uk/bot.php?+',
        'Exabot': 'http://www.exabot.com/go/robot',
        'Heritrix': 'http://www.archive.org/details/archive.org_bot)'}

count_brousers = {}
for i in brousers.keys():
    count_brousers[i] = 0
for j in mobile_brousers.keys():
    count_brousers[j] = 0

count_search = {}
for k in search_systems.keys():
    count_search[k] = 0

count_bots = {}
for g in bots.keys():
    count_bots[g] = 0

all_request_count = 0

pattern_unic_address = re.compile(r' - - ')
pattern_times = re.compile(r'\d+\/\w+\/\d+\:\d+\:\d+\:\d+\s\+\d+')


def pattern_protocols(line):
    protocol = pattern_unic_address.split(line)
    protocol = pattern_times.split(protocol[1])
    protocol = re.split(r'\]\s\"', protocol[1])
    protocol = re.split(r'\s\"', protocol[1], maxsplit=1)
    return protocol


def pattern_system(line):
    system = pattern_protocols(line)
    if system[1][0] == '-':
        sys = re.split(r'\-\s\"', system[1])
    else:
        sys = re.split(r'\w+.+\"\s\"', system[1])
    return sys


def pattern_agents(line):
    agents = pattern_system(line)
    if len(agents) == 2:
        agent = re.split(r'\w+\/.+\s\(.+\)\s', agents[1])
    else:
        agent = re.split(r'\w+\/.+\s\(.+\)\s', agents[0])
    return agent


unic_ip_addresses = set()


def unic_address(line):
    ip = pattern_unic_address.split(line)
    unic_ip_addresses.add(ip[0])
    return unic_ip_addresses


list_date = []
set_date = set()


def date(line):
    date_time = pattern_times.findall(line)
    date = re.findall(r'\d+\/\w+\/\d+',date_time[0])
    list_date.append(date[0])
    set_date.add(date[0])
    return set_date


list_time = []


def time(line):
    time = pattern_times.findall(line)
    list_time.append(time[0])
    return list_time

list_protocol = []


def protocol(line):
    protocol = pattern_protocols(line)
    list_protocol.append(protocol[0])
    return list_protocol

list_referers = []
not_url = 0


def referer(line):
    protocol = pattern_protocols(line)
    if protocol[1][0] == '-':
        global not_url
        not_url += 1
    else:
        list_referer = re.findall(r'\w+.+\"\s\"', protocol[1])
        list_referers.append(list_referer[0])

list_system = []
no_inform_syst = 0


def system(line):
    sys = pattern_system(line)
    if len(sys) == 2:
        system = re.findall(r'\w+\/.+\s\(.+\)\s', sys[1])
    else:
        system = re.findall(r'\w+\/.+\s\(.+\)\s', sys[0])
    if system == []:
        global no_inform_syst
        no_inform_syst += 1
    else:
        list_system.append(system[0])

list_agent = []
list_bots_research = []
count_true = 0

k_key = {}


def agents(line):
    global list_agent
    global count_true
    agent = pattern_agents(line)
    if len(agent) == 2:
        count_true += 1
        agents = re.findall(r'\w+.+\n', agent[1])
        if agents != []:
            if agents[0].find('(') != -1:
                agen = re.split(r'\s\(.+\)\"\n', agents[0])
                list_agent = agen[0].split(' ')
            else:
                list_agent = agents[0].split(' ')   
        if re.findall(r'\w+\:\/+\w+\.\w+.+\n', agent[1]):
            agents = re.findall(r'\w+\:\/+\w+\.\w+.+\n', agent[1])
            list_bots_research.append(agents[0])
        return list_agent
    else:
        a = re.findall(r'\w+\:\/+\w+\.\w+.+\n', agent[0])
        if a != []:
            list_bots_research.append(a[0])
        list_agent = agent[0].split(' ')
        return list_agent


request_agents = []


date_brousers = dict()
counter_dbrousers = collections.Counter()
date_mobale_brousers = dict()
counter_mbrousers = collections.Counter()
date_searche_system = dict()
counter_ssystem = collections.Counter()
date_bots = dict()
counter_bots = collections.Counter()



def count_date_brousers(line, set_date, key, diction_f, count_f):
    for date in set_date:
        if line.find(date) != -1:
            if not diction_f.get(date):
                diction_f[date] = dict()
            if not diction_f.get(date).get(key):
                diction_f[date][key] = 0
            diction_f[date][key] = diction_f.get(date).get(key) + 1
            count_f[date] += 1
            break


def analysis(brousers, request_agents, line):
    for key in brousers.keys():
        if len(brousers.get(key)) != len(request_agents):
            continue
        is_find = True
        for agent in brousers.get(key):
            if not find_agent(request_agents, agent):
                is_find = False
                break
        if is_find:
            count_brousers[key] = count_brousers.get(key) + 1
            count_date_brousers(line, set_date, key, date_brousers, counter_dbrousers)
            k_key[all_request_count] = key


def analysis_mobile(brousers, line):
    global count_true
    for key in brousers.keys():
        is_find = True
        for agent in brousers.get(key):
            if line.find(agent) == -1:
                is_find = False
                break
        if is_find:
            count_brousers[key] = count_brousers.get(key) + 1
            count_true += 1
            count_date_brousers(line, set_date, key, date_mobale_brousers, counter_mbrousers)
            k_key[all_request_count] = key
            


def analysis_systems_bots(count, brousers, line, date_info, counter_info):
    for key in brousers.keys():
        is_find = True
        if line.find(brousers[key]) == -1:
            is_find = False
            continue
        if is_find:
            count[key] = count.get(key) + 1
            count_date_brousers(line, set_date, key, date_info, counter_info)
            #k_key[all_request_count] = key


def find_agent(agents, value):
    for agent in agents:
        if agent.find(value) != -1:
            return True
    return False


list_ip_date = []
set_ip_date = set()
pattern_ip_date = re.compile(r'\d+\.\d+\.\d+\.\d+\s\-\s\-\s\[\d+\/\w+\/\d+')


def ip_date(line):
    ip_date = pattern_ip_date.findall(line)
    list_ip_date.append(ip_date[0])
    set_ip_date.add(ip_date[0])
    return set_ip_date


def save_data(file_name, list_values, strings):
    os.makedirs('logs', exist_ok=True)
    folder_logs = os.path.abspath('.\\logs\\' + file_name)
    fl = open(folder_logs, 'w')
    for value in list_values:
        fl.write(value)
        fl.write('\n')
    size_bytes = os.path.getsize(folder_logs)
    if size_bytes != 0:
        print(f'{strings} сохранен в файл {file_name} размером '
              f'{size_bytes} байт')


def main(*, debug_msg=True, debug_save=True):
    l_count_del = 0
    global k_key
    k_key = {}
    with open(folder_apache_logs, 'r') as fp:
        for line in fp.readlines():
            global all_request_count
            all_request_count += 1  # кол-во запросов

            unic_ip = unic_address(line)  # список уникальных IP

            date(line)  # список уникальной даты

            time(line)  # список даты и времени

            ip_date(line)  # список IP и даты

            protocol(line)  # список протоколов

            referer(line)  # список URL-запросов

            system(line)  # информация о системе
            analysis_mobile(mobile_brousers, line)
            analysis_systems_bots(count_search, search_systems, line, date_searche_system, counter_ssystem)
            analysis_systems_bots(count_bots, bots, line, date_bots, counter_bots)
            agent = agents(line)
            if agent is not None:
                l_count_del += 1

            analysis(brousers, list_agent, line)

        set_bots_research = set()
        for i in list_bots_research:
            bot = re.split(r'\"\n', i)
            bot = re.split(r'\;', bot[0])
            bot = re.split(r'\)', bot[0])
            set_bots_research.add(bot[0])

        if debug_msg:
            print(f'Список уникальных запросов в файле {f}: {unic_ip}')
            print(f'Количество запросов в файле {f} = {all_request_count}')
            print(f'Количество уникальных запросов в файле {f} = {len(unic_ip)}')

            print(f'Кол-во URL-запроса: {len(list_referers)}')
            print(f'Нет URL-запроса: {not_url}')
            print(f'Известно информации от систем: {len(list_system)}')
            print(f'Нет информации о системе: {no_inform_syst}')

            print(f'Количество запросов от браузеров, в том числе с мобильных:\n'
                  f'{count_brousers}')
        num = 0
        for key in count_brousers.keys():
            num += count_brousers.get(key)
        # print(num)

        if debug_msg:
            print(f'Количество запросов от поисковых систем:\n'
                  f'{count_search}')
        num2 = 0
        for key in count_search.keys():
            num2 += count_search.get(key)
        # print(num2)

        if debug_msg:
            print(f'Список ботов и кол-во их запросов:\n'
                  f'{count_bots}')
        num3 = 0
        for key in count_bots.keys():
            num3 += count_bots.get(key)
        # print(num3)

        if debug_save:
            save_data('unic_ip.txt', unic_ip, 'Список уникальных ip')
            save_data('date_time.txt', list_time, 'Список даты и времени')
            save_data('protocols.txt', list_protocol, 'Список протоколов')
            save_data('referers.txt', list_referers, 'Список запросов')
            save_data('information_system.txt', list_system,
                            'Список информации от систем')

if __name__ == "__main__":
    main()

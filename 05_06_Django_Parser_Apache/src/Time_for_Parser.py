from Parser_Apache_logs import Ratomskaya_parser_apache_logs as Parser
import os
import collections
import datetime
import pytz



script_path = os.path.dirname(__file__)
Parser.path_file_apache = script_path + '\\apache_logs\\' + Parser.f

folder_apache_logs = os.path.abspath(Parser.path_file_apache)


dtime_object_set = set()


def translate_f_t_time(list_date):
    for i in list_date:
        dtime = datetime.datetime.strptime(i, '%d/%B/%Y')
        dtime_object_set.add(datetime.datetime.strftime(dtime, '%Y.%m.%d'))
    return dtime_object_set


def print_date_info(date_dict, count_info, string_info):
    print(f'------------------------------------------------',
          f'Информация о дате и {string_info}',
          f'------------------------------------------------')
    count = 0
    for k in date_dict.keys():
        print(f'{k} было зафиксированно запросов от следующих {string_info}:')
        print(f'{date_dict[k]}\n')
        for k2 in date_dict[k].keys():
            count += date_dict[k][k2]

    save_reports(name_save, 'Было зафиксированно запросов от ', dict(date_dict), string_info)
    print(f'Общее кол-во запросов от {string_info} = {count}')
    save_reports(name_save, 'Общее кол-во запросов от ', str(count), string_info)
    print(f'Общее кол-во запросов от {string_info} по дням {dict(count_info)}')
    save_reports(name_save, 'Общее кол-во запросов по дням от ', dict(count_info), string_info)


def save_reports(file_name, strings, list_date, var=''):
    os.makedirs('reports', exist_ok=True)
    folder_logs = os.path.abspath('.\\reports\\' + file_name)
    with open(folder_logs, 'a') as report:
        if type(list_date) == dict:
            report.write(strings)
            report.write(var)
            report.write(': ')
            report.write('\n')
            for k in list_date.keys():
                report.write(k)
                report.write(': ')
                report.write(str(list_date.get(k)))
                report.write('\n')
        elif type(list_date) == str:
            report.write(strings)
            report.write(var)
            report.write(': ')
            report.write(list_date)
            report.write('\n')
        else:
            report.write(strings)
            report.write(': ')
            report.write('\n')
            for value in list_date:
                report.write(value)
                report.write('\n')


#  Создание имени файла отчета(текущее дата/время + имя лога(без расширения) + .txt)
time = datetime.datetime.now()
direct = os.path.abspath(__file__)
time = str(time)
time = time.replace(':', '_')
name_save = time[0: 19] + '_' + Parser.f + '.txt'


def main(save_logs=True):
    Parser.main(debug_msg=False, debug_save=False)
    print('------------------------------------------------'\
        'Информация о дате и IP-адресах'\
        '------------------------------------------------')

    translate_f_t_time(Parser.set_date)
    counter_date = collections.Counter()
    print(f'Список уникальных дат: {dtime_object_set}')
    save_reports(name_save, 'Список уникальных дат', dtime_object_set)
    for date in Parser.list_date:
        counter_date[date] += 1

    #
    time = []
    tz = set()
    utc = set()
    for t in range(0, len(Parser.list_time)):
        d_t = datetime.datetime.strptime(Parser.list_time[t], '%d/%B/%Y:%H:%M:%S %z')
        tz.add(str(d_t.tzname()))
        utc.add(str(d_t.utcoffset()))
        time.append(str(d_t))
        
    if save_logs:
        Parser.save_data('date-time_not_string.txt', time, 'Список даты и времени (альтернативная запись)')
    print(f'Дата выводится в формате {tz}. {tz} = {utc}')
    #
    
    print(f'Количество упоминаний даты: {dict(counter_date)}')
    save_reports(name_save, 'Количество упоминаний даты', dict(counter_date))
    counter_value_date = 0
    for value in counter_date.values():
        counter_value_date += value
        
    print(f'Общее кол-во дат: {counter_value_date}')
    save_reports(name_save, 'Общее кол-во дат', str(counter_value_date))
        
    #print(len(list_ip_date))
    print(f'Кол-во уникальных пар дата-время {len(Parser.set_ip_date)}')
    save_reports(name_save, 'Кол-во уникальных пар дата-время', str(len(Parser.set_ip_date)))

    counter_date.clear()

    for d in Parser.set_date:
        for ip in Parser.set_ip_date:
            if ip.find(d) != -1:
                counter_date[d] += 1

    print(f'Количество уникальных запросов по датам: {dict(counter_date)}')
    save_reports(name_save, 'Количество уникальных запросов по датам', dict(counter_date))
    if save_logs:
        Parser.save_data('unic_ip_date.txt', Parser.set_ip_date, 'Список уникальных пар IP-дата')

    #print(date_brousers)
    print_date_info(Parser.date_brousers, Parser.counter_dbrousers, 'десктопных браузерах')

    print_date_info(Parser.date_mobale_brousers, Parser.counter_mbrousers, 'мобильных браузерах')

    print_date_info(Parser.date_searche_system, Parser.counter_ssystem, 'поисковых систем')

    print_date_info(Parser.date_bots, Parser.counter_bots, 'ботов')

    folder_logs = os.path.abspath('.\\reports\\' + name_save)
    size_bytes = os.path.getsize(folder_logs)
    folder_logs = os.path.split(folder_logs)
    if size_bytes != 0:
        print(f'Отчет по статистике сохранен сохранен в файл {name_save} размером '
              f'{size_bytes} байт в папку {folder_logs[0]}')
    return time



if __name__ == "__main__":
    main()

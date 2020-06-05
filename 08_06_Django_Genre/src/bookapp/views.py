from django.shortcuts import render
from django.http import HttpResponse
import random
import datetime
#import requests
from . models import Genre
from . forms import GenreForm


# Create your views here.

def test(request):
    """s = requests.get('https://www.nbrb.by/api/exrates/rates?periodicity=0')
    result = s.json()
    rate = {}
    for d in result:
        if d.get('Cur_Abbreviation') == 'USD':
            rate['USD'] = d.get('Cur_OfficialRate') * d.get('Cur_Scale')
        elif d.get('Cur_Abbreviation') == 'EUR':
            rate['EUR'] = d.get('Cur_OfficialRate') * d.get('Cur_Scale')
        elif d.get('Cur_Abbreviation') == 'RUB':
            rate['RUB'] = d.get('Cur_OfficialRate') * d.get('Cur_Scale')
    r = random.randint(0, 100)
    l = [1, 2, 3, 4, 5]
    date = datetime.datetime.now()
    context = {'some_value': l, 'time': date, 'happy_number': r, 'USD': rate.get('USD'), 'EUR': rate.get('EUR'), 'RUB': rate.get('RUB'), 'rate': rate}
    """
    # get one obj from Genre
    #genre = Genre.objects.get(pk=1)
    #genre2 = Genre.objects.filter(name='ужасы')
    #books = Genre.objects.all()
    #context = {'genre': genre, 'genre2': genre2, 'books':books}
    form = GenreForm()
    return render(request, template_name='bookapp/index.html', context={'form':form})
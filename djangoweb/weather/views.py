from django.shortcuts import render
from django.http import HttpResponse
import requests
import datetime
import math

def home(request):
    api_key = '2d41c22ae78b3bd082fd3f0eda60e983'
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Dallas&appid='+api_key
    r = requests.get(url)
    j = r.json()

    url2 = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=Dallas&cnt=16&units=imperial&appid='+api_key
    r2 = requests.get(url2)
    j2=r2.json()
    weekly_data = {}
    for entry in j2['list']:
        dt = datetime.datetime.fromtimestamp(entry['dt'])
        dt2 = dt.strftime('%a %m-%d')
        print(entry)

        weekly_data[dt2] = [entry['temp']['max'], entry['temp']['min'], entry['weather'][0]  ['main'], math.floor(entry['pop']*100)]

    context = {'main': j['weather'][0]['main'], 'min':weekly_data}
    return render(request, 'home.html', context)

# Create your views here.

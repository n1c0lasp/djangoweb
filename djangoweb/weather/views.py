from django.shortcuts import render
from django.http import HttpResponse
import requests
import datetime

def home(request):
    api_key = '2d41c22ae78b3bd082fd3f0eda60e983'
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Dallas&appid='+api_key
    r = requests.get(url)
    j = r.json()

    url2 = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=Dallas&cnt=16&appid='+api_key
    r2 = requests.get(url2)
    j2=r2.json()
    print (j2)
    weekly_data = {}
    for entry in j2['list']:
        dt = datetime.datetime.fromtimestamp(entry['dt'])
        dt2 = dt.strftime('%Y-%m-%d %H:%M:%S')
        weekly_data[dt2] = 0

    print(weekly_data)
    context = {'main': j['weather'][0]['main']}
    return render(request, 'home.html', context)

# Create your views here.

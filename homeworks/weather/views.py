from django.shortcuts import render
from django.http import HttpResponse
import  urllib, json
import json
import requests
# Create your views here.


def get_weather(request):
    response = []
    response2 =[]
    response3 = []
    response4 =[]
    response5 = []
    count = 0
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                           params={'id': 524901, 'units': 'metric', 'lang': 'ru', 'APPID': "650d2f741c3a94ff67826dc0c4441728"})
        data = res.json()
        for i in data['list']:
            if count < 3:
               response.append(
                   str('{0:+3.0f}'.format(i['main']['temp']))+ str(i['weather'][0]['description']))
            if count > 2 and count <6:
               response2.append(
                   str('{0:+3.0f}'.format(i['main']['temp'])) + str(i['weather'][0]['description']))
            if count > 5 and count < 9:
                response3.append(
                    str('{0:+3.0f}'.format(i['main']['temp'])) + str(i['weather'][0]['description']))
            if count > 8 and count < 12:
                response4.append(str('{0:+3.0f}'.format(i['main']['temp'])) + str(i['weather'][0]['description']))
            if count > 11 and count < 15:
                response5.append(
                    str('{0:+3.0f}'.format(i['main']['temp'])) + str(i['weather'][0]['description']))
            count += 1
        return render(request, 'weather/weather.html', {
                'weathers': response,
                'weathers2': response2,
                'weathers3': response3,
                'weathers4': response4,
                'weathers5': response5,
        })
       #return HttpResponse(response)
    except Exception as e:
        print("Exception (forecast):", e)
        pass


def get_currency(request):
    payload = {'Content-Type': 'text/json'}
    r = requests.get("https://api.fixer.io/latest?base=RUB", params=payload)
    currency = r.json()
    response = 'RUB-USD ' + str(currency['rates']['USD']) + 'RUB-EUR ' + str(currency['rates']['EUR'])
    return render(request, 'weather/currenty.html', {
        'currency': response,
    })

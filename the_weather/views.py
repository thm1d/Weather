import requests
from django.shortcuts import render
from decouple import config

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + config('API_KEY')
    city = 'Pabna'

    r = requests.get(url.format(city)).json()
    #print(r.text)

    city_weather = {
        'city' : city,
        'temperature' : r['main']['temp'],
        'description' : r['weather'][0]['description'],
        'icon' : r['weather'][0]['icon'],
    }

    print(city_weather)

    context = {'city_weather' : city_weather}
    return render(request, 'the_weather/weather.html', context)

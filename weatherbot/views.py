from django.shortcuts import render
import requests

def index(request):
    # Your index view logic here
    return render(request, 'weatherbot/index.html')

def weather_report(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = 'e83342bbfe53cc1ef24c77614910bfd8'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            weather_info = {
                'city': data['name'],
                'main': data['weather'][0]['main'],
                'temp': data['main']['temp'],
                'max_temp': data['main']['temp_max'],
                'min_temp': data['main']['temp_min'],
                'feels_like': data['main']['feels_like'],
            }
            return render(request, 'weatherbot/weather_report.html', {'weather_info': weather_info})
        else:
            error_message = data.get('message', 'Unknown error')
            return render(request, 'weatherbot/error.html', {'error_message': error_message})

    return render(request, 'weatherbot/index.html')

from django.shortcuts import render

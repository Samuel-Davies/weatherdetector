from django.shortcuts import render

import json 
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        # the request we are sending to open weathermaps
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=492072660c9ba5e44ab7040fdde6ce17').read()
        
        # data i get after sending a request
        json_data = json.loads(res)

        # changing json_data input a distionary so it can be easily accessed 
        data = {
            'country_code' : str(json_data['sys']['country']),
            'coordinate' : str(json_data['coord']['lon']) + ' ' + 
            str(json_data['coord']['lat']),
            'temp': str(json_data['main']['temp']) + 'k',
            'pressure': str(json_data['main']['pressure']),
            'humidity': str(json_data['main']['humidity']), 


        }
    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city': city,'data':data})

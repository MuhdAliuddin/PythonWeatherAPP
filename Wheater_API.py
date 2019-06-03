'''

    PARADIGM PROJECT (PYTHON WEATHER APP)

    Muhammad Aliuddin b. Refakaei A161177

    
    
'''
import sys
import requests
import json

class WeatherAPI():

    ### API KEY : #b34980d5a9be7409bbd8275123e1da05

    def weather_key(city):

        weatherKey = 'b34980d5a9be7409bbd8275123e1da05'
        url = 'https://api.openweathermap.org/data/2.5/forecast'

        params = {'APPID': weatherKey, 'q':city, 'units': 'metric'}
        response = requests.get(url, params=params)
        weatherResults = response.json()

        return weatherResults
    
    
    def temp_results(weatherResults):

        temp = weatherResults['list'][0]['main']
        current_temp = weatherResults['list'][0]['main']['temp']
        min_temp = weatherResults['list'][0]['main']['temp_min']
        max_temp = weatherResults['list'][0]['main']['temp_max']
        humid_level = weatherResults['list'][0]['main']['humidity']

        return current_temp, min_temp, max_temp, humid_level


    def weather_results(weatherResults):
    
        weather_current = weatherResults['list'][0]['weather'][0]['main']
        weather_desc = weatherResults['list'][0]['weather'][0]['description']

        return weather_current, weather_desc


    sys._excepthook = sys.excepthook

    def application_exception_hook(exctype, value, traceback):

        '''
        Error exception handling
        '''
        
        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)

    sys.excepthook = application_exception_hook

        

        

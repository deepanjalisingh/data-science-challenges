# pylint: disable=missing-module-docstring

import sys
import urllib.parse
import requests

BASE_URI = "https://www.metaweather.com"


def search_city(query):
    '''Look for a given city and disambiguate between several candidates. Return one city (or None)'''
    url = "https://www.metaweather.com/api/location/search/?query="+query
    response = requests.get(url).json()
    if response and len(response)>0:
        city = response[0]
        return city
    print('City not found')

def weather_forecast(woeid):
    '''Return a 5-element list of weather forecast for a given woeid'''
    url = "https://www.metaweather.com/api/location/"+str(woeid)
    response = requests.get(url).json()
    consolidated_weather=response['consolidated_weather']
    result=[]
    for weather in consolidated_weather:
        d={}
        d['applicable_date']=weather['applicable_date']
        d['weather_state_name']=weather['weather_state_name']
        d['max_temp']=weather['max_temp']
        result.append(d)
    return result



def main():
    '''Ask user for a city and display weather forecast'''
    query = input("City?\n> ")
    city = search_city(query)
    if city:
        woeid=city['woeid']
        x=weather_forecast(woeid)
        print("Here's the weather in " + query)
        for day in x:
            print(str(day['applicable_date'])+ ":",
                  day['weather_state_name'],
                  str(day['max_temp'])+ "°C")

if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit(0)

import math
import requests

DbugMode = False

# print(response['main']['temp'] - 273.15)

with open('API/keyWeather.txt', 'r') as file:
    key = file.read()

def getWeather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}'
    response = requests.get(url).json()
    if DbugMode:
        print(response)
    getValue(response)

def getLocation():
    location = input('Enter the city: ')
    getWeather(location)

def getValue(response):
    print(response.keys())
    value = input('What value do you want to get? ')
    try:
        print(response[value][0].keys())
    except:
        print(response[value].keys())
    data = input(f'What data do you want to get from {value}? ')
    try:
        print(response[value][0][data])
    except:
        print(response[value][data])

if __name__ == '__main__':
    getLocation()
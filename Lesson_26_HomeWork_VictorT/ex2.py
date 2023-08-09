"""
Use a combination of 2 WEB APIs, to create an application that will find the country and city
using the IP Example and will show the weather data using this.

The program should automatically detect the location and display the weather when started.

It should show:

    City, Country
    Temperature (celsius)
    Weather (example: Cloudy/Clear/Snowing/Raining)

"""

import requests


def get_ip():
    ip_address = input("Please input your IP: ")
    return ip_address


def weather_api():
    with open('weather_api.txt', 'r') as file:
        content = file.read()
        return content


def geolocation():
    url = "https://weatherapi-com.p.rapidapi.com/ip.json"

    querystring = {"q": get_ip()}

    headers = {
        "X-RapidAPI-Key": weather_api(),
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())
    # location = response.json()
    # latitude = location['lat']
    # longitude = location['lon']
    # return latitude, longitude


def get_weather():
    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring = {"q": geolocation()}

    headers = {
        "X-RapidAPI-Key": weather_api(),
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())

    # data = response.json()
    # condition = data['current']['condition']['text']
    # print(condition)


get_weather()

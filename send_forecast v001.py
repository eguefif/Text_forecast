import requests
import pprint
import json
from datetime import datetime as dt
from dateutil import tz
from twilio.rest import Client
import sys


def get_geoloc(city):
    key = "Your openweathermap API key"
    url = f"https://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={key}"

    response = requests.get(url)
    data = response.json()

    return data[0]['lat'], data[0]['lon']

def forecast(body, city):
    body += '\nToday\n'
    key = "Your openweathermap API key"
    lat, lon = get_geoloc(city)

    # Getting the forecast
    api_url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=Metric&appid={key}"
    response = requests.get(api_url)
    data = response.json()

    # Determine lowest and highest temperature and conition
    low = 200
    high = 0
    conditions = ''
    for i in range(4):
        if data['list'][i]['main']['temp_min'] < low:
            low = data['list'][i]['main']['temp_min']

        if data['list'][i]['main']['temp_max'] > high:
            high = data['list'][i]['main']['temp_max']

        conditions += data['list'][i]['weather'][0]['main'] + ' '

    body += 'Low: ' + str(low) + 'c ' + 'max: ' + str(high) + 'c\n' + conditions

    return body


def send(body):
    date = dt.now(tz=tz.tzlocal())

    account_sid = 'Tzillio SID'
    secret = 'your Twillio secret code'
    client = Client(account_sid, secret)
    message = client.messages.create(
        from_='+12484505852',
        to='+17784440795',
        body=body,
    )

    print(f'Message sent on {date}')
    return


def now(city):
    # Todo: check for the province and country
    body = f'\nNow in {city}:\n'
    key = "Your openweathermap API key"

    lat, lon = get_geoloc(city)

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=Metric&appid={key}"
    response = requests.get(url)

    data = response.json()
    body += str(data['weather'][0]['main']) + ' '
    body += str(data['main']['temp']) + 'c'

    return body

# The program starts here
if len(sys.argv) > 1:
    city = sys.argv[1]
else:
    city = 'Victoria'

body = now(city)
body = forecast(body, city)

send(body)

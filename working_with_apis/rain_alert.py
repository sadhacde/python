'''
This program check if there is rain in the next 12 hours at the location provided
through lat/long coordinates. If so, it will send a whatsapp message notification.
Runs on pythonanywhere.com everyday at a set time.
'''

import requests
import os
from twilio.rest import Client

LAT = 33.0198
LON = -96.6989

api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACC_SID")
auth_token = os.environ.get("AUTH_TOKEN")

parameters = {
    "lat": LAT,
    "lon": LON,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

# print(weather_data["list"][0]["weather"][0]['id'])
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_="whatsapp:...",
    body="It's going to rain today. Remember to bring an umbrella",
    to="whatsapp:..."
    )
    print(message.status)

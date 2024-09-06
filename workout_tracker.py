'''
tracks workout through nutritionx api which calculates calories burned in workout,
ex: I ran for 20 minutes would be saved as 129~ calories
data from nutritionx is then saved in google sheets through sheety api
'''

import requests
import os
from datetime import datetime

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")

exc_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
exc_params = {
    "query": input("What excercises did you do today? "),
    "gender": #female/male,
    "weight_kg": #int,
    "height_cm": #int,
    "age": #int
}

response = requests.post(url=exc_endpoint, json=exc_params, headers=headers)
result = response.json()

today = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

sheety_endpoint = "https://api.sheety.co/..."

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs)
    print(sheet_response.text)

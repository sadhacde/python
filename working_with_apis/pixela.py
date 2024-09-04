'''
habit tracker using https://pixe.la/ API
creates profile, graph, and updates it with pixels
'''
import requests
import os
from datetime import datetime

TOKEN = os.environ.get("TOKEN")
USERNAME = os.environ.get("USERNAME")
GRAPH_ID = os.environ.get("GRAPH_ID")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# creates a new user profile
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# creates a new graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "meditation",
    "unit": "minutes",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# https://pixe.la/v1/users/<username>/graphs/<graph_id>.html

# can either post or delete a new pixel
pixel_record_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now().strftime("%Y%m%d")
pixel_record = {
    "date": today,
    "quantity": input("How many minutes did you meditate for? ")
}

pixel_change_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
response = requests.post(url=pixel_record_endpoint, json=pixel_record, headers=headers)
print(response.text) # was successful or not

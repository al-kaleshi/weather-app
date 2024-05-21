
import datetime as dt
import pytz
import requests
import matplotlib.pyplot as plt
import pandas as pd


url = "secret"
headers = {"accept": "application/json"}
response = requests.get(url, headers=headers)
weather_data = response.json()

data = weather_data['data']['values']
location = weather_data['location']['name']

time = weather_data['data']['time']
cloud_base = data['cloudBase']
cloud_ceiling = data['cloudCeiling']
cloud_cover = data['cloudCover']
dew_point = data['dewPoint']
humidity = data['humidity']
temperature = data['temperature']
wind_speed = data['windSpeed']


class Request:
    def __init__(self, url, headers):
        self._url = url
        self._headers = headers
        
    @property
    def Url(self):
        return self._url
    
    @property
    def Headers(self):
        return self._headers
    
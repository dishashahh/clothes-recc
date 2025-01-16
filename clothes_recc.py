# Access weather API to extract max temp, min temp and rainfall

### Work in Progress ###
import requests

def fetchForecast(lat, lon, apikey):
    url = "https://api.tomorrow.io/v4/weather/realtime?location=42.3478,-71.0466&apikey=zcnw8nghwYPKVCSkZ32ewexg5LOjZ1gr"
    querystring = {"values":"humidity"}
    return requests.get(url, params=querystring)
    # return response.json() 

def consumeOne(forecast):
    return {
    "temp": forecast["temp"]["value"],
    "feel": forecast["feels_like"]["value"],
    "precipitation": forecast["precipitation"]["value"],
    "precipitation_type": forecast["precipitation_type"]["value"],
    "weather_code": forecast["weather_code"]["value"],
    }

print(fetchForecast(144.9631,37.8136,"zcnw8nghwYPKVCSkZ32ewexg5LOjZ1gr"))


import requests

url = "https://api.tomorrow.io/v4/weather/realtime?location=toronto&apikey=zcnw8nghwYPKVCSkZ32ewexg5LOjZ1gr"

headers = {
    "accept": "application/json",
    "accept-encoding": "deflate, gzip, br"
}

response = requests.get(url, headers=headers)

# print(response.text)
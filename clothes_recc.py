# Access weather API to extract max temp, min temp and rainfall

### Work in Progress ###
import requests

url = "https://api.tomorrow.io/v4/weather/forecast?location=melbourne&timesteps=1h&units=metric&apikey=zcnw8nghwYPKVCSkZ32ewexg5LOjZ1gr"

headers = {
    "accept": "application/json",
    "accept-encoding": "deflate, gzip, br"
    }

response = requests.get(url, headers=headers)
res_json = response.json()

# Extract hourly forecast data
hourly_data = res_json["timelines"]["hourly"]

# Print hourly temperature for next 10 hours
for i in range(10):
    print(hourly_data[i]["values"]["temperature"])

# Check precipitationProbability to determine weather umbrella is required
# if 0<PP<30 - might need an umbrella today
# if PP>=30 - definitely will require an umbrella today!
# TODO

# Check uvIndex to determine if sunscreen and a hat is required
# if UV> 3 --> sunscreen required
# if UV > 7 --> bring a hat
# TODO

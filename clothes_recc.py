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
def temp():
    max_temp = 0
    min_temp = 100
    for i in range(10):
        hourly_temp = hourly_data[i]["values"]["temperature"]
        if hourly_temp < min_temp:
            min_temp = hourly_temp
        if hourly_temp > max_temp:
            max_temp = hourly_temp
    # Output
    print("Today the maximum temperature will be "+str(int(max_temp))+"°C, with a minimum of "+str(int(min_temp))+"°C.")
    
    if max_temp>=25:
        print("Its a warm day today, you should wear shorts and a t-shirt.")
    elif 18<=max_temp<25:
        print("It will be a pleasant day - pants and a top will be your best bet.")
    elif 12<=max_temp<18:
        print("A chilly day today, you should wear pants and a jacket.")
    elif max_temp<12:
        print("BRR its a cold day, remember to layer up!")
    
    if min_temp<18 and max_temp>18:
        print("But it will get cold at times, carry a light jacket.")

print(temp())
        
# Check precipitationProbability to determine weather umbrella is required
# if 0<PP<30 - might need an umbrella today
# if PP>=30 - definitely will require an umbrella today!
def rain_prob():
    for i in range(10):
        hourly_rain_prob = hourly_data[i]["values"]["precipitationProbability"]
        print (hourly_rain_prob)


# Check uvIndex to determine if sunscreen and a hat is required
# if UV> 3 --> sunscreen required
# if UV > 7 --> bring a hat
# TODO

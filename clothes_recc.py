'''
This code recommends to the user the clothes they should wear based on weather forecasts in Melbourne.
Code considers temperature, precipitation probability and UV index.

Time complexity: O(1)
The code iterates through 10 hours of weather forecasting. Since it is a fixed number of hours, the complexity is O(1).

Code written by Disha Shah.
'''

import requests

# Weather API to access weather forecasts in Melbourne
url = "https://api.tomorrow.io/v4/weather/forecast?location=melbourne&timesteps=1h&units=metric&apikey=zcnw8nghwYPKVCSkZ32ewexg5LOjZ1gr"

headers = {
    "accept": "application/json",
    "accept-encoding": "deflate, gzip, br"
    }

# Generate JSON file of hourly weather predictions
response = requests.get(url, headers=headers)
res_json = response.json()

# Extract hourly forecast data
hourly_data = res_json["timelines"]["hourly"]

def temp()->str:
    '''
    This function returns outfit recommendations based on maximum and minimum temperatures.

    Inputs: 
        None

    Outputs:
        str: temperatuer and outfit recommendation
    '''
    max_temp = 0
    min_temp = 100
    # Determine max and min temperature for the next 10 hours
    for i in range(10):
        hourly_temp = hourly_data[i]["values"]["temperature"]
        if hourly_temp < min_temp:
            min_temp = hourly_temp
        if hourly_temp > max_temp:
            max_temp = hourly_temp

    # Print max and min temp
    print("Today the maximum temperature will be "+str(int(max_temp))+"°C, with a minimum of "+str(int(min_temp))+"°C.")
    
    # Recommend outfit based on temperature
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

        
def rain_prob()->str:
    '''
    This function checks precipitation probability and recommends umbrella or not accordingly

    Inputs: 
        None

    Outputs:
        str: string recommending umbrella or not 
    '''
    rain_prob = 0
    for i in range(10):
        hourly_rain_prob = hourly_data[i]["values"]["precipitationProbability"]
        if hourly_rain_prob > rain_prob:
            rain_prob = hourly_rain_prob # update rain probability
    if 0<rain_prob<30: # Chance of an umbrella if precipitation is below 30%
        print("You also may need an umbrella today. There is a chance of rain.")
    elif rain_prob>=30: # Umbrella definitely required is rain_prob > 30%
        print("Also, bring an umbrella with you. It will likely rain.")


def uv_index() -> str:
    '''
    This function checks UV index and recommends sun protection 

    Inputs: 
        None

    Outputs:
        str: string recommending type of sun protection (if needed)
    '''
    uv = 0
    for i in range(10):
        hourly_uv = hourly_data[i]["values"]["uvIndex"]
        if hourly_uv > uv:
            uv = hourly_uv
    if uv>7:
        print("The UV is high today, wear sunscreen and bring a hat.")
    elif uv>3:
        print("Wear sunscreen to protect yourself from the sun's rays.")


# Call each function, and get recommendations on what clothes to wear.
temp()
rain_prob()
uv_index()
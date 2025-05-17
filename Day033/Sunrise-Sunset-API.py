# API Parameters: unlike some API's like ISS posiion or kanye-quote APi, 
# there are some parameter which require certain parameters to get a specific response

# Along with passing parameters in get method, parameters can also be send in the URL
#  like: https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400&date=today  After the ? parameters are given


import requests


MY_LONG = 73.047882 #74.324875
MY_LAT = 33.684422 #35.912967
parameters = { #parameters being passed must be in dict form and the key and values must be acc. to API Documentation
    "lat" : MY_LAT,
    "lng" : MY_LONG,
    # "formatted" : 0  # this shows the sunrise , sunset timing in 24 hour format from 0 to 24, unlike 0 to 12 in default formatted : 1
}

response_API = requests.get(url="https://api.sunrise-sunset.org/json", params= parameters)
response_API.raise_for_status()

response_data = response_API.json()  # response data from API after request

print(response_data)

sunrise_time = response_data["results"]["sunrise"]
print(f"Sunrise time: {sunrise_time}")

sunrise_time_list= sunrise_time.split(":")
print(sunrise_time_list)
sunrise_hour = sunrise_time_list[0]
print(f"Sunrise hour: {sunrise_hour}")
# API: is a interface through which a system or a software can interact with another software, without the need for how the other software works

# API endpoint : it is the address of the API that we want to use and request functions (it is in json format)
# API request : it a way to connect and get use of the API, python library "requests" is a popular module to call API's in python

# Request Status code : whenever request is send to an API a response is expected this response is given in the form of 
#request status codes, these are codes in numerical form which each has special meaning to it, like 200: every think went right, 404: error, not found
# ------- request status codes ------- https://www.webfx.com/web-development/glossary/http-status-codes/ (website to understand request codes)
# 1XX : Hold On , wait for a while this response in not final
# 2XX : Here you go , everything went fine and response it ready
# 3XX : Go away , not authorised to view response
# 4XX : You screwed up , response does not exist
# 5XX : I screwed up , error in server

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json") # get method calls an API through API endpoint

response.raise_for_status() # this method helps show any error that occured and raises an error, when request status code other than 2XX appear

API_data = response.json() #json contains the data relatedd to API
print(API_data)

longitude= API_data["iss_position"]["longitude"]
latitude= API_data["iss_position"]["latitude"]
print(f"--- ISS Location ---\nLongitude: {longitude}\nLatitude: {latitude}")
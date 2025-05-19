# ADD QUIZZLER DATABASE API 

import requests
 
API_ENDPOINT = "https://opentdb.com/api.php"
parameters = { # can either pass the paramters dict in param or in URL inself
    "amount" : 10,       # read documentation of API to know which parameters to pass
    "type": "boolean",
    "category": 18
}

response_api = requests.get(url=API_ENDPOINT, params=parameters)
response_api.raise_for_status()

API_data = response_api.json()
# print(API_data)  #need to remove response code here

question_data = API_data["results"]  
print(question_data)
print("\n\n")
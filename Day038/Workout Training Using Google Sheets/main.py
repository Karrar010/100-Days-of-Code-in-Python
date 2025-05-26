import requests
from datetime import datetime

NUTRITIONIX_API_ID = "8faf6b18"
NUTRITIONIX_API_KEY = "a03bdcf2f659ae490cb8940b46c446c9"
SHEETY_API_AUTH = "Basic WWFzaGt1bjpzaGVldHkueWFzaDE="
GOOGLE_SHEET_NAME = "workout"
Nutritionix_API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
Sheety_Endpoint = "https://api.sheety.co/282b3cb23d661caeb8b1cbee35c9943e/myWorkoutsTracker/workouts"

# Step 1 - Setup API Credentials and Google Spreadsheet
Nutritionix_Params = {
    "query" : input("Tell me what exercise you did and its duration(mins): ")
}
Nutritionix_header = {  # It is method to authenticate the User
    'Content-Type': 'application/json',
    "x-app-id" : NUTRITIONIX_API_ID,
    "x-app-key" : NUTRITIONIX_API_KEY
}


# Step 2 - Get Exercise Stats with Natural Language Queries
response_Nutritionix = requests.post(url= Nutritionix_API_ENDPOINT, json= Nutritionix_Params, headers= Nutritionix_header)
print(response_Nutritionix.json()["exercises"])

Current_Date = datetime.now().strftime("%d/%m/%Y")
Current_Time = datetime.now().strftime("%H:%M:%S")

for x in range(len(response_Nutritionix.json()["exercises"])):  # When we enter more than one exercise in input

    Exercise_Name = response_Nutritionix.json()["exercises"][x]["name"].title()  # For tilte casing the text
    Duration_Exercise = response_Nutritionix.json()["exercises"][x]["duration_min"]
    Calories_Burn = response_Nutritionix.json()["exercises"][x]["nf_calories"]
    print(f"\nLength of List of Exercise Input: {len(response_Nutritionix.json()['exercises'])}\nDate: {Current_Date}\nTime: {Current_Time}\nExercise: {Exercise_Name}\nDuration: {Duration_Exercise}\nCalories: {Calories_Burn}")


# Step 3 - Setup Your Google Sheet with Sheety
    Sheety_API_Params = {
        GOOGLE_SHEET_NAME: {
            "date" : Current_Date,
            "time" : Current_Time,
            "exercise" : Exercise_Name,
            "duration" : Duration_Exercise,
            "calories" : Calories_Burn
        }
    }
# Step 4 - Saving Data into Google Sheets(Using Post)
# Step 5 - Authenticate Your Sheety API
    Sheety_Header = {
        'Content-Type': 'application/json',
        "Authorization" : SHEETY_API_AUTH
    }
    response_Sheety = requests.post(url=Sheety_Endpoint, json=Sheety_API_Params,headers= Sheety_Header)
    print(f"\n Added Row in Sheets:\n{response_Sheety.text}") # To check for each post()/add of new row in sheets
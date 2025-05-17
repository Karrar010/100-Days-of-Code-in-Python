import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 33.684422 # Your latitude
MY_LONG = 74.324875 # Your longitude
SENDER_EMAIL = "me@gmail.com"
RECIPIENT_EMAIL = "me@gmail.com"
PASS  = "*****"

# FOR COMPUTER POSITION
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
#Your position is within +5 or -5 degrees of the ISS position.

# FOR CHECKING SUNSET SUNRISE DETAILS
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
# print(sunset)
time_now = datetime.now()
hour_today = time_now.hour


# If the ISS is close to my current position and it is currently dark
def iss_overhead_notifier():
    if (MY_LAT - 5) < iss_latitude > (MY_LAT + 5) and (MY_LONG - 5) < iss_longitude < (MY_LONG + 5) :
        if hour_today >= sunset or hour_today <= sunrise:
            return True
        

# Then send me an email to tell me to look up. BONUS: run the code every 60 seconds.
while True:
    time.sleep(60) # this will check every 60 sec when code runs and will send email when conditions matches
    if iss_overhead_notifier():
        with smtplib.SMTP(host="smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user= SENDER_EMAIL,password= PASS)
            connection.sendmail(
                from_addr= SENDER_EMAIL,
                to_addrs = RECIPIENT_EMAIL,
                msg= "Subject: ISS NOTIFIER\n\nLook Up ISS is Right Above you Champ."
        )
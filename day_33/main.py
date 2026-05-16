import requests
import smtplib
import threading
from datetime import datetime

MY_LAT = 31.200092 # Your latitude
MY_LONG = 29.918739 # Your longitude
EMAIL = "jo.mohsen2@gmail.com"
PASSWORD = "jccvfjvhesamzuhn"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "date":"today",
    "formatted": 0,
}

def check_iss(params:dict):
    threading.Timer(60.0, check_iss,[params]).start()
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    data = iss_response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    su_sr_response = requests.get("https://api.sunrise-sunset.org/json", params=params)
    su_sr_response.raise_for_status()
    data = su_sr_response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = int(datetime.now().strftime("%H"))


    is_night = (time_now > sunset) or (time_now < sunrise) or (time_now == 0)
    is_iss_within_range = (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5)
    print(f"Night Time:{is_night}\nISS In Range:{is_iss_within_range}")
    if is_night and is_iss_within_range:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=str("jo.muhsen3@gmail.com"),
                msg=f"Subject: ISS Is In Range!\n\n The ISS is within your location!",
            )
    else:
        print("The ISS is not within location")

    #If the ISS is close to my current position
    # and it is currently dark
    # Then send me an email to tell me to look up.
    # BONUS: run the code every 60 seconds.


check_iss(parameters)

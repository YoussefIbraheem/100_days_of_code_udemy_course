import requests
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText


def check_weather_and_send_email():
    params = {
        "q": "Alexandria,Egypt",
        "appid": "b94fbec31f9257ffbe37f8b89b069f59",
        "cnt": 4,
    }

    ow_api = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?", params=params
    )
    ow_api.raise_for_status()

    # Check for rainy days in the next 4 days
    rainy_days = [w for w in ow_api.json()["weather"] if w["id"] < 700]

    if rainy_days:
        send_email("Bring an umbrella with you.")
    else:
        send_email("You won't be needing an umbrella soon")


def send_email(message):
    sender_email = "jo.mohsen2@gmail.com"
    receiver_email = "jo.muhsen3@gmail.com"
    password = "jccvfjvhesamzuhn"

    msg = MIMEText(message)
    msg["Subject"] = "Rainy Weather Alert"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())


check_weather_and_send_email()

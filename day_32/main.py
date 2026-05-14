import os
import random
import smtplib
from datetime import date

import pandas as pd

EMAIL = "jo.mohsen2@gmail.com"
PASSWORD = "jccvfjvhesamzuhn"

today = date.today()
birthdays = pd.read_csv("./birthdays.csv").dropna()
today_birthdays = birthdays[
    (birthdays["month"] == today.month) & (birthdays["day"] == today.day)
]

for _, person in today_birthdays.iterrows():
    template_file = random.choice(os.listdir("./letter_templates"))
    with open(f"./letter_templates/{template_file}") as f:
        template = f.read()

    message = template.replace("[NAME]", str(person["name"]))

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=str(person["email"]),
            msg=f"Subject: Happy Birthday\n\n{message}",
        )

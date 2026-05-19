import requests as req
import os
import textwrap
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

STOCK = "BLBD"
COMPANY_NAME = "Blue Bird Co."
ALPHAVANTAGE_API = "https://www.alphavantage.co/query"
NEWS_API = "https://newsapi.org/v2/everything"
ALPHAVANTAGE_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")


def get_stock_price(symbol: str):
    stk_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": "demo",  # Use your actual API key here
    }
    stk_pri_res = req.get(f"{ALPHAVANTAGE_API}", params=stk_params)
    stk_pri_res.raise_for_status()
    stk_pri_2_days = list(stk_pri_res.json()["Time Series (Daily)"].values())[:2]

    pri_lst_dy = float(stk_pri_2_days[0]["4. close"])
    pri_bef_dy = float(stk_pri_2_days[1]["4. close"])

    diff = pri_lst_dy - pri_bef_dy
    diff_per = diff / pri_bef_dy * 100

    return diff, diff_per


def get_news(symbol: str):
    news_params = {"apiKey": NEWS_API_KEY, "q": symbol}
    news_res = req.get(f"{NEWS_API}", params=news_params)
    news_res.raise_for_status()
    top_3_news = news_res.json()["articles"][:3]
    formatted_news = []
    for news in top_3_news:
        formatted_news.append(
            {
                "headline": news["title"],
                "brief": textwrap.shorten(news["description"], width=100),
                "url": news["url"],
            }
        )

    return formatted_news


def send_email(subject, body):

    sender = os.getenv("EMAIL_ADDRESS")
    receiver = os.getenv("RECEIVER_EMAIL_ADDRESS")
    password = os.getenv("EMAIL_PASSWORD")
    host = os.getenv("EMAIL_SMTP")
    port = os.getenv("EMAIL_PORT")

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = receiver
    msg.set_content(body)

    with smtplib.SMTP(host, port) as smtp:
        smtp.starttls()
        smtp.login(sender, password)
        smtp.send_message(from_addr=sender, to_addrs=receiver, msg=msg)


def main():
    
    diff, diff_per = get_stock_price(STOCK)

    if abs(diff_per) > 10:  # Check if the price changed by more than 5%
        news = get_news(STOCK)

        email_body = f"{STOCK}: {'+🔺' if diff_per > 0 else '-🔻'}{abs(diff_per):.2f}%\n"
        for n in news:
            email_body += (
                f"Headline: {n['headline']}\nBrief: {n['brief']}\nURL: {n['url']}\n\n"
            )

        send_email(f"{COMPANY_NAME} Stock Update", email_body)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error occurred: ", str(e))

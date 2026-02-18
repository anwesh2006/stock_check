import requests
import os

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

URL = "https://www.bigbasket.com/pd/40359270/"

def send_telegram(message):
    telegram_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(telegram_url, data=data)

def check_stock():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(URL, headers=headers)

    if "Add to basket" in response.text:
        send_telegram("🔥 Product is BACK IN STOCK!")
        print("Stock Found")
    else:
        print("Still Out of Stock")

check_stock()


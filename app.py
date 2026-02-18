import requests
import os

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

URL = "https://www.bigbasket.com/pd/40359270/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers)
html = response.text.lower()

# Check stock properly
if "sold out" not in html and "out of stock" not in html:
    message = "🔥 Protein wafer bar is IN STOCK!"
else:
    message = "❌ Still out of stock"

# Send Telegram message ONLY if in stock
if "in stock" in message.lower():
    requests.get(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        params={"chat_id": CHAT_ID, "text": message}
    )

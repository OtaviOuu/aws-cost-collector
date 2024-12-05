import requests
from dotenv import load_dotenv
import os

load_dotenv()


def send_message_to_telegram(message):

    bot_token = os.getenv("BOT_TOKEN")
    chanell_id = os.getenv("CHANELL_ID")

    base_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    try:
        requests.post(base_url, json={"chat_id": chanell_id, "text": message})
    except Exception as e:
        print(e)

import time
import requests

TELEGRAM_BOT_TOKEN = 'YOUR_BOT_TOKEN'
TELEGRAM_CHAT_ID = 'YOUR_CHAT_ID'
TIKTOK_USERNAME = '0211quoccuong'

def check_live():
    url = f"https://www.tiktok.com/@{TIKTOK_USERNAME}/live"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    return "is live" in res.text.lower() or 'LIVE' in res.text

def send_telegram_message(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": msg}
    requests.post(url, data=data)

sent = False
while True:
    try:
        if check_live() and not sent:
            send_telegram_message(f"{TIKTOK_USERNAME} is now LIVE on TikTok!")
            sent = True
        elif not check_live():
            sent = False
    except Exception as e:
        print("Error:", e)
    time.sleep(10)

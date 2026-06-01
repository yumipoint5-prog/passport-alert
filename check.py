from playwright.sync_api import sync_playwright
from datetime import datetime
import os

TARGET_URL = "https://sfyoyaku.rsvsys.jp/reservations/calendar"

def notify(message):
    os.system(f'''
    osascript -e 'display notification "{message}" with title "Passport Alert"'
    ''')

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto(TARGET_URL)

    content = page.content()

    
   keywords = [
    "○",
    "◯"
]
    

    found = any(k in content for k in keywords)

    # 条件追加
target_slots = [
    "06/11 15:00",
    "06/11 15:10",
    "06/11 15:20",
    "06/11 15:30",
    "06/11 15:40",
    "06/11 15:50",

    "06/12 13:00",
    "06/12 13:10",
    "06/12 13:20",
    "06/12 13:30",
    "06/12 13:40",
    "06/12 13:50",

    "06/12 14:00",
    "06/12 14:10",
    "06/12 14:20",
    "06/12 14:30",
    "06/12 14:40",
    "06/12 14:50",

    "06/12 15:00",
    "06/12 15:10",
    "06/12 15:20",
    "06/12 15:30",
    "06/12 15:40",
    "06/12 15:50",

    "06/12 16:00",
    "06/12 16:10",
    "06/12 16:20",
    "06/12 16:30",
    "06/12 16:40",
    "06/12 16:50",

    "06/12 17:00",
    "06/12 17:10",
    "06/12 17:20",
    "06/12 17:30",
    "06/12 17:40",
    "06/12 17:50",
]
    slot_found = any(slot in content for slot in target_slots)

    if found and slot_found:
        notify("希望日時にパスポート予約空きあり！")

    browser.close()

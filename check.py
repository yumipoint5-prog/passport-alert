from playwright.sync_api import sync_playwright
import requests
import os

URL = "https://sfyoyaku.rsvsys.jp"

WEBHOOK = os.environ.get("DISCORD_WEBHOOK")

TARGETS = [
    ("6/11", 15),
    ("6/12", 13),
]

def notify(msg):
    requests.post(WEBHOOK, json={
        "content": msg
    })

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    page.goto(URL, wait_until="networkidle")

    content = page.content()

    found_slots = []

    for date, hour in TARGETS:
        for h in range(hour, 24):
            patterns = [
                f"{date} {h}:00",
                f"{date} {h}時",
                f"{date}&nbsp;{h}",
            ]

            if any(p in content for p in patterns):
                found_slots.append(f"{date} {h}:00以降")

    if found_slots:
        notify(
            "予約空きの可能性:\n" +
            "\n".join(found_slots)
        )

    browser.close()from playwright.sync_api import sync_playwright
import requests
import os

URL = "https://sfyoyaku.rsvsys.jp"

WEBHOOK = os.environ.get("DISCORD_WEBHOOK")

TARGETS = [
    ("6/11", 15),
    ("6/12", 13),
]

def notify(msg):
    requests.post(WEBHOOK, json={
        "content": msg
    })

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    page.goto(URL, wait_until="networkidle")

    content = page.content()

    found_slots = []

    for date, hour in TARGETS:
        for h in range(hour, 24):
            patterns = [
                f"{date} {h}:00",
                f"{date} {h}時",
                f"{date}&nbsp;{h}",
            ]

            if any(p in content for p in patterns):
                found_slots.append(f"{date} {h}:00以降")

    if found_slots:
        notify(
            "予約空きの可能性:\n" +
            "\n".join(found_slots)
        )

    browser.close()from playwright.sync_api import sync_playwright
import requests
import os

URL = "https://sfyoyaku.rsvsys.jp"

WEBHOOK = os.environ.get("DISCORD_WEBHOOK")

TARGETS = [
    ("6/11", 15),
    ("6/12", 13),
]

def notify(msg):
    requests.post(WEBHOOK, json={
        "content": msg
    })

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    page.goto(URL, wait_until="networkidle")

    content = page.content()

    found_slots = []

    for date, hour in TARGETS:
        for h in range(hour, 24):
            patterns = [
                f"{date} {h}:00",
                f"{date} {h}時",
                f"{date}&nbsp;{h}",
            ]

            if any(p in content for p in patterns):
                found_slots.append(f"{date} {h}:00以降")

    if found_slots:
        notify(
            "予約空きの可能性:\n" +
            "\n".join(found_slots)
        )

    browser.close()from playwright.sync_api import sync_playwright
import requests
import os

URL = "https://sfyoyaku.rsvsys.jp"

WEBHOOK = os.environ.get("DISCORD_WEBHOOK")

TARGETS = [
    ("6/11", 15),
    ("6/12", 13),
]

def notify(msg):
    requests.post(WEBHOOK, json={
        "content": msg
    })

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    page.goto(URL, wait_until="networkidle")

    content = page.content()

    found_slots = []

    for date, hour in TARGETS:
        for h in range(hour, 24):
            patterns = [
                f"{date} {h}:00",
                f"{date} {h}時",
                f"{date}&nbsp;{h}",
            ]

            if any(p in content for p in patterns):
                found_slots.append(f"{date} {h}:00以降")

    if found_slots:
        notify(
            "予約空きの可能性:\n" +
            "\n".join(found_slots)
        )

    browser.close(from playwright.sync_api import sync_playwright
import requests
import os

URL = "https://sfyoyaku.rsvsys.jp"

WEBHOOK = os.environ.get("DISCORD_WEBHOOK")

TARGETS = [
    ("6/11", 15),
    ("6/12", 13),
]

def notify(msg):
    requests.post(WEBHOOK, json={
        "content": msg
    })

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    page.goto(URL, wait_until="networkidle")

    content = page.content()

    found_slots = []

    for date, hour in TARGETS:
        for h in range(hour, 24):
            patterns = [
                f"{date} {h}:00",
                f"{date} {h}時",
                f"{date}&nbsp;{h}",
            ]

        

WEBHOOK = os.environ.get("DISCORD_WEBHOOK")

def notify(msg):
    requests.post(WEBHOOK, json={
        "content": msg
    })

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    page.goto(URL, wait_until="networkidle")

   from playwright.sync_api import sync_playwright
import requests
import os

URL = "https://sfyoyaku.rsvsys.jp"

WEBHOOK = os.environ.get("DISCORD_WEBHOOK")

TARGETS = [
    ("6/11", 15),
    ("6/12", 13),
]

def notify(msg):
    requests.post(WEBHOOK, json={
        "content": msg
    })

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    page.goto(URL, wait_until="networkidle")

    content = page.content()

    found_slots = []

    for date, hour in TARGETS:
        for h in range(hour, 24):
            patterns = [
                f"{date} {h}:00",
                f"{date} {h}時",
                f"{date}&nbsp;{h}",
            ]

            if any(p in content for p in patterns):
                found_slots.append(f"{date} {h}:00以降")

    if found_slots:
        notify(
            "予約空きの可能性:\n" +
            "\n".join(found_slots)
        )

    browser.close()

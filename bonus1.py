import requests
import selectorlib
import smtplib, ssl
import time
import os
from datetime import datetime

URL = "https://programmer100.pythonanywhere.com"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract1.yaml")
    value = extractor.extract(source)["temperature"]
    return value


def store(extracted):
    with open('temperature.txt', 'a') as file:
        file.write(extracted + "\n")


def read(extracted):
    with open('data.txt', 'r') as file:
        return file.read()

if __name__ == "__main__":
    while True:
        now = datetime.now()
        czas = now.strftime('%Y-%m-%d-%H-%M-%S')
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(f"{czas},{extracted}")
        store(f"{czas},{extracted}")
        time.sleep(2)

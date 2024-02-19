import requests
import selectorlib
import smtplib, ssl
import time
import os
from datetime import datetime
import sqlite3

URL = "https://programmer100.pythonanywhere.com"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


connection = sqlite3.connect("bonus_data.db")

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
    row = extracted.split(",")
    row = [item.strip() for item in row]
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Temperatura VALUES(?,?)", row)
    connection.commit()


def read(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    date, temperature = row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Temperatura WHERE data=? AND temperatura=?", (date, temperature))
    rows = cursor.fetchall()
    print(rows)
    return rows

if __name__ == "__main__":
    while True:
        now = datetime.now()
        czas = now.strftime('%Y-%m-%d-%H-%M-%S')
        scraped = scrape(URL)
        extracted = extract(scraped)
        dane = f"{czas},{extracted}"
        row = read(dane)
        store(f"{czas},{extracted}")
        time.sleep(2)

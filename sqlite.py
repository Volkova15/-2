import sqlite3
import requests
from datetime import datetime

API_URL = "https://api.open-meteo.com/v1/forecast?latitude=50.45&longitude=30.52&current_weather=true"

def get_temperature():
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        return data["current_weather"]["temperature"]
    else:
        return None

conn = sqlite3.connect("weather.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS weather (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    datetime TEXT,
    temperature REAL
)
""")
conn.commit()

def save_temperature():
    temp = get_temperature()
    if temp is not None:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO weather (datetime, temperature) VALUES (?, ?)", (now, temp))
        conn.commit()
        print(f"Дані збережено: {now} - {temp}°C")
    else:
        print("Не вдалося отримати температуру")

save_temperature()
conn.close()

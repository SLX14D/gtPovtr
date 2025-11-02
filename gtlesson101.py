import requests
import sqlite3
from datetime import datetime
from bs4 import BeautifulSoup

URL = "https://www.gismeteo.kz/weather-astana-5164/now/"

conn = sqlite3.connect("weather.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS weather (
    datetime TEXT,
    temperature TEXT
)
""")
conn.commit()

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

temp_el = soup.find(class_="unit unit_temperature_c")

if temp_el:
    temperature = temp_el.text.strip()

else:
    temperature = "N/A"

current_dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
cur.execute("INSERT INTO weather (datetime, temperature) VALUES (?, ?)",
            (current_dt, temperature))
conn.commit()

print("\nИстория температур:")
for row in cur.execute("SELECT * FROM weather"):
    print(row)

conn.close()
print(f"\n✅ Даннaые сохранены: {current_dt} — {temperature}")
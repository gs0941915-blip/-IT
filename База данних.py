import sqlite3
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

# ---------------- БАЗА ДАННЫХ ----------------

conn = sqlite3.connect("weather.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS weather (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date_time TEXT,
    temperature TEXT
)
""")

conn.commit()

# ---------------- ПОЛУЧЕНИЕ ПОГОДЫ ----------------

def get_weather():
    try:
        # Сайт погоды
        url = "https://www.gismeteo.ua/ua/weather-dnipro-5070/"

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers)

        # Проверка подключения
        if response.status_code != 200:
            print("Ошибка подключения к сайту")
            return

        soup = BeautifulSoup(response.text, "html.parser")

        # Поиск температуры
        temp_element = soup.find("temperature-value")

        # Проверка найден ли элемент
        if temp_element is None:
            print("Температура не найдена")
            return

        temp = temp_element.get_text(strip=True)

        # Текущая дата и время
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Запись в базу данных
        cursor.execute("""
        INSERT INTO weather (date_time, temperature)
        VALUES (?, ?)
        """, (now, temp))

        conn.commit()

        print(f"[+] Данные добавлены: {now} | Температура: {temp}")

    except Exception as e:
        print("Ошибка:", e)

# ---------------- АВТООБНОВЛЕНИЕ ----------------

print("Программа запущена. Обновление каждые 30 минут.")

while True:
    get_weather()

    # 30 минут = 1800 секунд
    time.sleep(1800)
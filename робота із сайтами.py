import requests
from bs4 import BeautifulSoup

# Сайт
url = "http://books.toscrape.com/"

# Запрос к сайту
response = requests.get(url)

# Парсинг HTML
soup = BeautifulSoup(response.text, "html.parser")

# Все книги
books = soup.find_all("article", class_="product_pod")

print("----- СПИСОК КНИГ -----\n")

for book in books:
    # Название книги
    title = book.h3.a["title"]

    # Цена книги
    price = book.find("p", class_="price_color").text

    # Наличие
    availability = book.find("p", class_="instock availability").text.strip()

    print(f"Название: {title}")
    print(f"Цена: {price}")
    print(f"Наличие: {availability}")
    print("-" * 40)
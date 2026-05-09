import tkinter as tk
from tkinter import ttk, messagebox
import requests

url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"

response = requests.get(url)
rates_data = response.json()

rates = {"UAH": 1}

for item in rates_data:
    rates[item["cc"]] = item["rate"]

def convert_currency():
    try:
        amount = float(entry_amount.get())

        from_currency = combo_from.get()
        to_currency = combo_to.get()

        amount_in_uah = amount * rates[from_currency]
        result = amount_in_uah / rates[to_currency]

        label_result.config(
            text=f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}"
        )

    except ValueError:
        messagebox.showerror("Помилка", "Введіть правильне число!")

root = tk.Tk()
root.title("Конвертер валют НБУ")
root.geometry("400x300")
root.resizable(False, False)

label_title = tk.Label(
    root,
    text="Конвертер валют",
    font=("Arial", 18, "bold")
)
label_title.pack(pady=10)

entry_amount = tk.Entry(root, font=("Arial", 14))
entry_amount.pack(pady=10)

currencies = sorted(rates.keys())

combo_from = ttk.Combobox(root, values=currencies, font=("Arial", 12))
combo_from.set("USD")
combo_from.pack(pady=5)

combo_to = ttk.Combobox(root, values=currencies, font=("Arial", 12))
combo_to.set("UAH")
combo_to.pack(pady=5)

button_convert = tk.Button(
    root,
    text="Конвертувати",
    font=("Arial", 12),
    command=convert_currency
)
button_convert.pack(pady=15)

label_result = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold")
)
label_result.pack(pady=10)

root.mainloop()
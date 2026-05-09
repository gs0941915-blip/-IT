import tkinter as tk
from tkinter import messagebox
import sqlite3
import datetime
import matplotlib.pyplot as plt
from collections import defaultdict

# ---------------- ПАЛІТРА ----------------
PEACH = "#FF9A86"
ORANGE = "#FFB399"
YELLOW = "#FFD6A6"
CREAM = "#FFF0BE"
TEXT_DARK = "#3a3a3a"

# ---------------- ЕМОДЗІ ----------------
emoji_map = {
    "Хліб": "🍞",
    "Молоко": "🥛",
    "Шоколад": "🍫",
    "Вода": "💧",
    "Печиво": "🍪",
    "М'ясо": "🥩"
}

# ---------------- БАЗА ДАНИХ ----------------
conn = sqlite3.connect("shop_game.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price INTEGER,
    quantity INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS receipts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    total INTEGER,
    items TEXT
)
""")

# Заповнюємо базу тільки якщо вона порожня
cursor.execute("SELECT COUNT(*) FROM products")
if cursor.fetchone()[0] == 0:
    products_init = [
        ("Хліб", 20, 10),
        ("Молоко", 35, 8),
        ("Шоколад", 50, 5),
        ("Вода", 10, 20),
        ("Печиво", 30, 40),
        ("М'ясо", 70, 10)
    ]
    cursor.executemany("INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)", products_init)
    conn.commit()

money = 1000
cart = {}

# ---------------- ВІКНО ----------------
window = tk.Tk()
window.title("Магазин")
window.geometry("800x700")
window.config(bg=CREAM)


# ---------------- ФУНКЦІЇ ----------------

def update_products():
    product_list.delete(0, tk.END)
    cursor.execute("SELECT * FROM products")
    items = cursor.fetchall()
    for item in items:
        pid, name, price, qty = item
        emoji = emoji_map.get(name, "🛒")
        product_list.insert(tk.END, f"ID {pid} | {emoji} {name} | {price} грн | {qty} шт")
    balance_label.config(text=f"Баланс: {money} грн")


def add_to_cart():
    # 1. Перевірка вибору у списку
    selection = product_list.curselection()
    if not selection:
        messagebox.showerror("Помилка", "Будь ласка, оберіть товар зі списку!")
        return

    # 2. Перевірка коректності числа
    try:
        amount = int(amount_entry.get())
        if amount <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Помилка", "Введіть коректну кількість (ціле число більше 0)!")
        return

    selected_text = product_list.get(selection[0])
    try:
        product_id = int(selected_text.split("|")[0].replace("ID", "").strip())

        cursor.execute("SELECT name, price, quantity FROM products WHERE id=? ", (product_id,))
        product = cursor.fetchone()

        if product:
            name, price, qty = product
            # Перевірка наявності на складі (з врахуванням того, що вже в кошику)
            already_in_cart = cart.get(product_id, {}).get("amount", 0)

            if amount + already_in_cart <= qty:
                if product_id in cart:
                    cart[product_id]["amount"] += amount
                else:
                    cart[product_id] = {"name": name, "price": price, "amount": amount}

                amount_entry.delete(0, tk.END)  # Очищуємо поле після успіху
                update_cart()
            else:
                messagebox.showerror("Помилка",
                                     f"На складі лише {qty} шт. Ви намагаєтесь додати разом: {amount + already_in_cart}")
    except Exception as e:
        messagebox.showerror("Помилка", f"Сталася помилка: {e}")


def update_cart():
    cart_list.delete(0, tk.END)
    for pid, item in cart.items():
        emoji = emoji_map.get(item["name"], "🛒")
        total = item["price"] * item["amount"]
        cart_list.insert(tk.END, f"{emoji} {item['name']} | {item['amount']} шт. | Разом: {total} грн")


def save_receipt(total_cost, items_text):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO receipts (date, total, items) VALUES (?, ?, ?)", (date, total_cost, items_text))
    conn.commit()


def show_chart():
    cursor.execute("SELECT date, total FROM receipts")
    data = cursor.fetchall()
    if not data:
        messagebox.showinfo("Графік", "Історія покупок порожня")
        return

    daily = defaultdict(int)
    for date, total in data:
        day = date.split(" ")[0]
        daily[day] += total

    dates = list(daily.keys())
    values = list(daily.values())

    plt.figure(figsize=(8, 5))
    plt.plot(dates, values, marker="o", color="orange", linewidth=2)
    plt.title("Витрати по днях")
    plt.xlabel("Дата")
    plt.ylabel("Сума (грн)")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def show_receipts():
    win = tk.Toplevel(window)
    win.title("Історія чеків")
    win.geometry("500x400")
    win.config(bg=CREAM)

    listbox = tk.Listbox(win, width=70, height=20, font=("Courier", 10))
    listbox.pack(pady=10, padx=10)

    cursor.execute("SELECT * FROM receipts ORDER BY id DESC")
    receipts = cursor.fetchall()

    for r in receipts:
        listbox.insert(tk.END, f"🧾 Чек №{r[0]} | {r[1]}")
        listbox.insert(tk.END, f"   Товари: {r[3]}")
        listbox.insert(tk.END, f"   СУМА: {r[2]} грн")
        listbox.insert(tk.END, "-" * 40)


def buy_cart():
    global money
    if not cart:
        messagebox.showerror("Помилка", "Кошик порожній!")
        return

    total_cost = sum(item["amount"] * item["price"] for item in cart.values())

    if money < total_cost:
        messagebox.showerror("Помилка", "Недостатньо грошей на балансі!")
        return

    # Оновлюємо базу даних
    items_summary = []
    for pid, item in cart.items():
        cursor.execute("SELECT quantity FROM products WHERE id=?", (pid,))
        current_qty = cursor.fetchone()[0]
        cursor.execute("UPDATE products SET quantity = ? WHERE id = ?", (current_qty - item["amount"], pid))
        items_summary.append(f"{item['name']} (x{item['amount']})")

    money -= total_cost
    save_receipt(total_cost, ", ".join(items_summary))

    cart.clear()
    update_cart()
    update_products()
    messagebox.showinfo("Успіх", f"Покупка здійснена! Списано: {total_cost} грн")


def clear_cart():
    if messagebox.askyesno("Очищення", "Ви дійсно хочете очистити кошик?"):
        cart.clear()
        update_cart()


# ---------------- UI ----------------

title = tk.Label(window, text="🛒 Магазин", font=("Arial", 22, "bold"), bg=CREAM, fg=TEXT_DARK)
title.pack(pady=5)

balance_label = tk.Label(window, text=f"Баланс: {money} грн", font=("Arial", 14, "bold"), bg=CREAM, fg="#2D5A27")
balance_label.pack()

tk.Label(window, text="Оберіть товар у списку:", bg=CREAM).pack()
product_list = tk.Listbox(window, width=80, height=8, font=("Arial", 11), bg=YELLOW, fg=TEXT_DARK,
                          selectbackground=ORANGE)
product_list.pack(pady=5)

tk.Label(window, text="Введіть кількість:", bg=CREAM).pack()
amount_entry = tk.Entry(window, font=("Arial", 12), width=10, justify='center')
amount_entry.pack(pady=5)
amount_entry.insert(0, "1")

tk.Button(window, text="➕ Додати в кошик", bg=PEACH, font=("Arial", 10, "bold"), command=add_to_cart).pack(pady=5)

tk.Label(window, text="🧺 Ваш кошик:", bg=CREAM, font=("Arial", 14, "bold")).pack(pady=5)
cart_list = tk.Listbox(window, width=80, height=6, bg="white")
cart_list.pack()

# Кнопки керування
btn_frame = tk.Frame(window, bg=CREAM)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="💰 КУПИТИ", bg="#90EE90", width=15, font=("Arial", 10, "bold"), command=buy_cart).grid(row=0,
                                                                                                                 column=0,
                                                                                                                 padx=5)
tk.Button(btn_frame, text="🧹 ОЧИСТИТИ", bg="#FF6347", width=15, command=clear_cart).grid(row=0, column=1, padx=5)

hist_frame = tk.Frame(window, bg=CREAM)
hist_frame.pack()

tk.Button(hist_frame, text="📜 Історія", width=15, command=show_receipts).grid(row=0, column=0, padx=5, pady=5)
tk.Button(hist_frame, text="📊 Графік", width=15, command=show_chart).grid(row=0, column=1, padx=5, pady=5)

update_products()

window.mainloop()
conn.close()
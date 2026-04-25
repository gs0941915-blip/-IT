result = []

def divider(a, b):
    if a < b:
        raise ValueError("a < b")
    if b > 100:
        raise IndexError("b > 100")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}  # прибрали []

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except Exception as e:
        print(f"Помилка для {key}: {type(e).__name__} - {e}")

print("Результат:", result)
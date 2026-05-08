import logging

logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d"
)


def decorator(func):
    def wrapper(*args, **kwargs):
        print("Calling decorated function")

        try:
            result = func(*args, **kwargs)
            print("Результат:", result)
            return result

        except ZeroDivisionError:
            logging.error("Ділення на нуль!")
            print("Помилка: не можна ділити на нуль")

        except SyntaxError:
            logging.error("Неправильний математичний вираз")
            print("Помилка: неправильний вираз")

        except Exception as e:
            logging.error(f"Сталася помилка: {e}")
            print("Невідома помилка")

    return wrapper


@decorator
def calculate(expression):
    return eval(expression)


calculate("10 + 5")
calculate("8 * 7")
calculate("20 / 0")
calculate("5 + ")
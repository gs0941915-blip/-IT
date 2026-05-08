#Завдання 1

import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d"
)


def sayHello():
    print("Hello")


sayHello()


def decorator(func):
    def wrapper(*args, **kwargs):
        print("Calling decorated function")

        logging.info("Функція була викликана")

        result = func(*args, **kwargs)
        return result

    return wrapper


@decorator
def say_Hello():
    print("Hello")


say_Hello()

#Завдання 2

import logging

logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d"
)

def sayHello():
    print("Hello")

sayHello()

def decorator(func):
    def wrapper(*args, **kwargs):
        print("Calling decorated function")
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            logging.error(f"Сталася помилка: {e}")
    return wrapper

@decorator
def say_Hello():
    print("Hello")
    x = 10 / 0   # спеціально викликаємо помилку

say_Hello()

#Завдання 3

def sayHello():
    print("Hello")


sayHello()


def decorator(func):
    def wrapper(*args, **kwargs):
        print("Calling decorated function")
        try:
            result = func(*args, **kwargs)
            return result
        except AssertionError:
            print("Невірне ім'я користувача або пароль")

    return wrapper


@decorator
def login(username, password):
    correct_username = "admin"
    correct_password = "1234"

    assert username == correct_username and password == correct_password

    print("Вхід виконано успішно")


login("admin", "1234")
login("user", "1111")


#Завдання 4
def sayHello():
    print("Hello")


sayHello()


def decorator(func):
    def wrapper(*args, **kwargs):
        print("Calling decorated function")
        try:
            result = func(*args, **kwargs)
            return result
        except AssertionError:
            print("Вам має бути 18 років або більше")

    return wrapper


@decorator
def check_age(age):

    assert age >= 18

    print("Ви можете використовувати цей сервіс")



check_age(20)
check_age(15)

#Завдання 5
def sayHello():
    print("Hello")


sayHello()


def decorator(func):
    def wrapper(*args, **kwargs):
        print("Calling decorated function")
        try:
            result = func(*args, **kwargs)
            return result
        except AssertionError:
            print("Список повинен містити принаймні 3 елементи")

    return wrapper


@decorator
def process_list(input_list):
    assert len(input_list) >= 3

    print(f"Список містить {len(input_list)} елементів")


process_list([1, 2, 3, 4])
process_list([1, 2])
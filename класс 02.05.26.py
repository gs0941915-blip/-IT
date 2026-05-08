def sayHello():
    print("Hello")

sayHello()

def decorator(func):
    def wrapper():
        print("Calling decorated function")
        func()


    return wrapper


def say_Hello():
    print("Hello")



say_Hello()

proSayHello = decorator(say_Hello)
proSayHello()

def decorator(func):
    def wrapper(*args, **kwargs):
        print("Calling decorated function")
        result = func(*args, **kwargs)
        return result
    return wrapper
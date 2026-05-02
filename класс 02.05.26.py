def sayHello():
    print("Hello")

sayHello()

def decorator(func):
    def wrapper():
        print("Calling decorated function")
        func()


    return wrapper

@decorator
def say_Hello():
    print("Hello")



say_Hello()
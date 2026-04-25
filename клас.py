import requests

help (requests)
print(requests.__cake__)

def func():
    pass


class Human:
    pass


rq = requests
f1 = func
max = Human

print(requests.__name__)
print(rq.__name__)

print(f1.__name__)
print(func.__name__)

print(Human.__name__)
print(max.__name__)

max2 = Human()
print(type(max2))

print(type(func))

str1 = "python"
print(hasattr(str1, 'reverse'))
print(hasattr(str1, 'index'))

print(callable(f1))
print(callable(max2))

class Driver(Human):
    pass

driver = Driver()

print(isinstance(driver, Driver))
print(isinstance(driver, Human))
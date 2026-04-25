#Перше завдання
num = 10
text = "Hello, Python!"
my_list = [1, 2, 3, 4]

print(type(num))
print(type(text))
print(type(my_list))

def my_function():
    pass

class MyClass:
    pass

obj = MyClass()

print(type(my_function))
print(type(MyClass))
print(type(obj))



#Друге завдання
text = "python"
numbers = [1, 2, 3]

def func():
    pass

class Human:
    def speak(self):
        print("Hello")

person = Human()

print(hasattr(text, 'upper'))
print(hasattr(text, 'append'))

print(hasattr(numbers, 'append'))
print(hasattr(numbers, 'clear'))

print(hasattr(func, '__call__'))

print(hasattr(person, 'speak'))
print(hasattr(person, 'run'))



#Трете завдання
text = "hello"

method1 = getattr(text, "upper")
print(method1())

method2 = getattr(text, "replace")
print(method2("l", "*"))

numbers = [1, 2, 3]

method3 = getattr(numbers, "append")
method3(4)
print(numbers)

class Human:
    def speak(self):
        return "Hi!"

person = Human()

method4 = getattr(person, "speak")
print(method4())



#Четверте завдання
def explore(obj):
    print("Об'єкт:", obj)
    print("Тип:", type(obj))
    print("Методи:", dir(obj))
    print("Має довжину:", hasattr(obj, "__len__"))
    print("-" * 40)


explore("hello")
explore([1, 2, 3])
explore(42)


def func():
    pass

class Human:
    def speak(self):
        return "Hi!"

person = Human()

explore(func)
explore(Human)
explore(person)

from datetime import datetime

class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def get_age(self):
        current_year = datetime.now().year
        return current_year - self.birth_year

    def show_info(self):
        print(f"Ім'я: {self.name}, Вік: {self.get_age()}")


class Driver(Person):
    def __init__(self, name, birth_year, license_number, experience):
        super().__init__(name, birth_year)
        self.license_number = license_number
        self.experience = experience

    def has_enough_experience(self):
        return self.experience > 2

    def show_info(self):
        print(f"Ім'я: {self.name}, Вік: {self.get_age()}, "
              f"№ посвідчення: {self.license_number}, "
              f"Стаж: {self.experience} років")


# Створення об'єктів
drivers = []

drivers.append(Driver("Олексій", 1995, "AB1234", 3))
drivers.append(Driver("Марія", 2000, "CD5678", 1))
drivers.append(Driver("Іван", 1988, "EF9012", 5))

# Вивід інформації
for driver in drivers:
    driver.show_info()
    if driver.has_enough_experience():
        print("✅ Достатній стаж водіння")
    else:
        print("❌ Недостатній стаж водіння")
    print()
###Завдання 1###

class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_done(self):
        self.completed = True

    def __str__(self):
        status = "✔ Виконано" if self.completed else "✘ Не виконано"
        return f"{self.title} | {self.deadline} | {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def del_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                return
        print(f"Завдання '{title}' не знайдено")

    def mark_task_done(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_done()
                return
        print(f"Завдання '{title}' не знайдено")

    def show_tasks(self):
        if not self.tasks:
            print("Список завдань порожній")
        for task in self.tasks:
            print(task)


# Приклад використання
manager = TaskManager()

manager.add_task(Task("Домашка", "Зробити математику", "25.04"))
manager.add_task(Task("Покупки", "Купити продукти", "24.04"))

manager.show_tasks()

print("\nПозначаємо 'Домашка' як виконане\n")
manager.mark_task_done("Домашка")
manager.show_tasks()

print("\nВидаляємо 'Покупки'\n")
manager.del_task("Покупки")
manager.show_tasks()
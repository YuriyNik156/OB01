class Task():
    def __init__(self):
        self.tasks = []

    def add_task(self, deadline, description):
        self.tasks.append({"deadline" : deadline,
                           "description" : description,
                           "status" : "Не выполнена"})

    def compltete_tasks(self, description):
        for task in self.tasks:
            if task["description"] == description:
                task["status"] = "Выполнена"
                print(f"Задача {description} выполнена")
            else:
                print(f"Задача {description} не найдена")

    def show_tasks(self):
        print("Текущие задачи")
        for task in self.tasks:
            if task["status"] == "Не выполнена":
                print(f"{task['description']} - {task['deadline']}")

t = Task()
t.add_task("01.04.2025", "Прочитать книгу")
t.add_task("05.04.2025", "Пробежать марафон")
t.add_task("27.04.2025", "Починить машину")

t.show_tasks()

t.compltete_tasks("Прочитать книгу")
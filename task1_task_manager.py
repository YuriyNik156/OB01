# Создай класс Task, который позволяет управлять задачами (делами). У задачи должны быть атрибуты: описание задачи,
# срок выполнения и статус (выполнено/не выполнено). Реализуй функцию для добавления задач, отметки выполненных задач
# и вывода списка текущих (не выполненных) задач.

class Task():
    def __init__(self):
        self.tasks = []

    def add_new_task(self):
        description = input("Введите описание задачи: ")
        deadline = input("Введите срок выполнения задачи: ")
        status_input = input("Введите 1, если задача выполнена или нажмите Enter")
        status = status_input == "1"

        self.tasks.append({"description" : description, "deadline" : deadline, "status" : status})
        print("Задача добавлена!")

    def mark_task_as_done(self):
        if not self.tasks:
            print("Нет задач для выполнения!")
            return

        print("\nВыберите номер задачи для отметки как выполненной:")
        for i, task in enumerate(self.tasks, start = 1):
            status_text = "Выполнена" if task["status"] else "Не выполнена"
            print(f"{i}. {task["description"]} - {status_text}")

        try:
            task_number = int(input("Введите номер задачи: ")) - 1
            if 0 <= task_number < len(self.tasks):
                self.tasks[task_number]["status"] = True
            else:
                print("Ошибка: некорректный номер задачи.")
        except ValueError:
            print("Ошибка: введите число!")

    def current_tasks(self):
        print("Текущие задачи: ")
        active_tasks = [task for task in self.tasks if not task["status"]]
        if active_tasks:
            for i, task in enumerate(active_tasks, start = 1):
                print(f"{i}. {task['description']} (Срок: {task['deadline']}) Не выполнена")
        else:
            print("Нет активных задач!")

task = Task()

while True:
    print("\nВыберите действие:")
    print("1 - Добавить задачу")
    print("2 - Отметить задачу как выполненную")
    print("3 - Показать текущие задачи")
    print("4 - Выход")

    choice = input("Введите номер действия: ")

    if choice == "1":
        task.add_new_task()
    elif choice == "2":
        task.mark_task_as_done()
    elif choice == "3":
        task.current_tasks()
    elif choice == "4":
        print(" Выход из программы.")
        break
    else:
        print(" Некорректный ввод! Попробуйте снова.")

# Создай класс Task, который позволяет управлять задачами (делами). У задачи должны быть атрибуты: описание задачи,
# срок выполнения и статус (выполнено/не выполнено). Реализуй функцию для добавления задач, отметки выполненных задач
# и вывода списка текущих (не выполненных) задач.

class Task():
    def __init__(self, description, deadline, status = False):
        self.description = description
        self.deadline = deadline
        self.status = status

    # Отметить выполненную задачу
    def mark_as_done(self):
        self.status = True
        print(f"Задача {self.description} выполнена. ")

    # Строковое представление задачи
    def __str__(self):
        status_text = "Выполнена" if self.status else "Не выполнена"
        return f"Описание задачи: {self.description} \n Срок выполнения задачи: {self.deadline} \n Статус задачи: {status_text}"

class TaskManager():
    def __init__(self):
        self.tasks = []

    def add_new_task(self):
        description = input("Введите описание задачи: ")
        deadline = input("Введите срок выполнения задачи: ")
        status_input = input("Введите 1, если задача выполнена или нажмите Enter")
        status = status_input == "1"

        new_task = Task(description, deadline, status)
        self.tasks.append(new_task)
        print("Задача добавлена!")

    def mark_task_as_done(self):
        if not self.tasks:
            print("Нет задач для выполнения!")
            return

        print("\nВыберите номер задачи для отметки как выполненной:")
        for i, task in enumerate(self.tasks, start=1):
            status_text = "Выполнена" if task.status else "Не выполнена"
            print(f"{i}. {task.description} - {status_text}")

        try:
            task_number = int(input("Введите номер задачи: ")) - 1
            if 0 <= task_number < len(self.tasks):
                self.tasks[task_number].mark_as_done()
            else:
                print("Ошибка: некорректный номер задачи.")
        except ValueError:
            print("Ошибка: введите число!")

    def current_tasks(self):
        print("Текущие задачи: ")
        active_tasks = [i for i in self.tasks if not i.status]
        if active_tasks:
            for i in active_tasks:
                print(i)
        else:
            print("Нет активных задач! ")

task_manager = TaskManager()

while True:
    print("\nВыберите действие:")
    print("1 - Добавить задачу")
    print("2 - Отметить задачу как выполненную")
    print("3 - Показать текущие задачи")
    print("4 - Выход")

    choice = input("Введите номер действия: ")

    if choice == "1":
        task_manager.add_new_task()
    elif choice == "2":
        task_manager.mark_task_as_done()
    elif choice == "3":
        task_manager.current_tasks()
    elif choice == "4":
        print(" Выход из программы.")
        break
    else:
        print(" Некорректный ввод! Попробуйте снова.")

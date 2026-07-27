from enum import Enum
from datetime import date

class Priority(Enum):
    Unspecified = 0
    High = 1
    Medium = 2
    Low = 3

class Task:
    def __init__(self, title, deadline, description, priority=Priority.Unspecified, done=False):
        self.title = title
        self._deadline = deadline
        self.description = description
        self.priority = priority
        self._done = done

    @property
    def deadline(self):
        return self._deadline
    
    @deadline.setter
    def deadline(self, value):
        if value > date.today():
            self._deadline = value
        else:
            raise ValueError("Дата дедлайна не может быть в прошлом")
    
    def is_overdue(self):
        if self._deadline < date.today() and self._done == False:
            return True
        return False

class TaskManager:
    def __init__(self):
        self._task_list = []

    def add_task(self, task):
        self._task_list.append(task)
    
    def get_all_tasks(self):
        return self._task_list.copy()
    
    def get_overdue_tasks(self):
        overdue_tasks = []
        for task in self._task_list.copy():
            if task.is_overdue():
                overdue_tasks.append(task)
        return overdue_tasks
    
    def remove_task(self, task):
        if task in self._task_list.copy():
            self._task_list.remove(task)

task1 = Task("Купить продукты", date(2026, 7, 27), "Купить молоко, хлеб и овощи", Priority.High, False)
task2 = Task("Выучить Python", date(2026, 7, 29), "Повторить Enum, циклы и функции", Priority.High, False)
task3 = Task("Убраться дома", date(2026, 7, 25), "Пропылесосить и помыть пол", Priority.Medium, False)
task4 = Task("Позвонить другу", date(2026, 7, 20), "Обсудить встречу на выходных", Priority.Low, False)
task5 = Task("Сделать проект Todo List", date(2026, 8, 1), "Добавить классы Task и список задач", Priority.High, False)
task6 = Task("Прочитать книгу", date(2026, 8, 5), "Прочитать 50 страниц", Priority.Medium, False)
task7 = Task("Спорт", date(2026, 7, 31), "Сделать тренировку 30 минут", Priority.Low, False)

task_manager = TaskManager()

tasks = [task1, task2, task3, task4, task5, task6, task7] 

for task in tasks:
    task_manager.add_task(task)

for task in task_manager.get_all_tasks():
    print(task.title)

for task in task_manager.get_overdue_tasks():
    print(task.title, task.deadline)

task_manager.remove_task(task1)

for task in task_manager.get_all_tasks():
    print(task.title)
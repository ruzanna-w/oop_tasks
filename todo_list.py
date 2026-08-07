from enum import Enum
from datetime import date, timedelta

class Priority(Enum):
    Unspecified = 0
    High = 1
    Medium = 2
    Low = 3

class RepeatInterval(Enum):
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"

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
    
    @property
    def done(self):
        return self._done
    
    @done.setter
    def done(self, value):
        if self._done == value:
            raise ValueError("Задача уже выполнена/открыта")
        self._done = value


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

    def complete_task(self, task):
        try:
            task.done = True
        except ValueError:
            print("Task has already completed")

    def reopen_task(self, task):
        try:
            task.done = False
        except ValueError:
            print("Task has already opened")

class RecurringTask(Task):
    def __init__(self, title, deadline, description, repeat_interval, priority=Priority.Unspecified, done=False):
        super().__init__(title, deadline, description, priority, done)
        self.repeat_interval = repeat_interval
    
    @Task.done.setter
    def done(self, value):
        # при переоткрытии задачи оставляю новый дедлайн, 
        # потому что может быть создана задача в прошлом, что рушит логику 
        overdue = self.is_overdue() 
        Task.done.fset(self, value)

        if value:
            if self.repeat_interval == RepeatInterval.WEEKLY:
                if overdue:
                    self.deadline = date.today() + timedelta(weeks=1)
                else:
                    self.deadline += timedelta(weeks=1)
        

task1 = Task("Купить продукты", date(2026, 8, 27), "Купить молоко, хлеб и овощи", Priority.High, False)
task2 = Task("Выучить Python", date(2026, 8, 29), "Повторить Enum, циклы и функции", Priority.High, False)
task3 = Task("Убраться дома", date(2026, 8, 25), "Пропылесосить и помыть пол", Priority.Medium, False)
task4 = Task("Позвонить другу", date(2026, 8, 20), "Обсудить встречу на выходных", Priority.Low, False)
task5 = Task("Сделать проект Todo List", date(2026, 8, 1), "Добавить классы Task и список задач", Priority.High, False)
task6 = Task("Прочитать книгу", date(2026, 8, 5), "Прочитать 50 страниц", Priority.Medium, False)
task7 = Task("Спорт", date(2026, 8, 31), "Сделать тренировку 30 минут", Priority.Low, False)
task8 = RecurringTask("Выучить Python Recurring", date(2026, 8, 29), "Повторить Enum, циклы и функции", RepeatInterval.WEEKLY, Priority.High, False)
task9 = RecurringTask("Сделать проект Todo List", date(2026, 7, 29), "Добавить классы Task и список задач", RepeatInterval.WEEKLY, Priority.High, False)
task10 = RecurringTask("Прочитать книгу", date(2026, 8, 5), "Прочитать 50 страниц", RepeatInterval.WEEKLY, Priority.Medium, False)
task11 = RecurringTask("Спорт", date(2026, 8, 31), "Сделать тренировку 30 минут", RepeatInterval.WEEKLY, Priority.Low, False)


task_manager = TaskManager()

tasks = [task1, task2, task3, task4, task5, task6, task7, task8, task9] 
recurring_tasks = [task8, task9, task10, task11]

for task in tasks:
    task_manager.add_task(task)

for task in task_manager.get_all_tasks():
    print(task.title)

for task in task_manager.get_overdue_tasks():
    print(task.title, task.deadline)

task_manager.remove_task(task1)

for task in task_manager.get_all_tasks():
    print(task.title)

print(f'У {task8.title} done = {task8.done}, deadline = {task8.deadline}')

task8.done = True
print(f'У {task8.title} done = {task8.done}, deadline = {task8.deadline}')

task8.done = False
print(f'У {task8.title} done = {task8.done}, deadline = {task8.deadline}')

task9.done = True
print(f'У {task9.title} done = {task9.done}, deadline = {task9.deadline}')

task10.done = True
print(f'У {task10.title} done = {task10.done}, deadline = {task10.deadline}')

task11.done = True
print(f'У {task11.title} done = {task11.done}, deadline = {task11.deadline}')

new_recurring_tasks = []

for task in recurring_tasks.copy():
    if task.done:
        new_rec_tasks = RecurringTask(
            task.title,
            task.deadline,
            task.description,
            task.repeat_interval,
            task.priority,
            False
        )
        new_recurring_tasks.append(new_rec_tasks)
    else:
        new_recurring_tasks.append(task)


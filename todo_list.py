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
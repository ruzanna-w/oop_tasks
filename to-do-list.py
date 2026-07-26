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
    
    def missed_task(self):
        if self._deadline < date.today() and self._done == False:
            return True
        else: False


    


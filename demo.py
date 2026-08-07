from todo_list import Priority, RepeatInterval, Task, TaskManager, RecurringTask
from datetime import date

RED = "\033[91m"
GREEN = "\033[92m"  
RESET = "\033[0m"    

task1 = Task("Купить продукты", date(2026, 8, 27), "Купить молоко, хлеб и овощи", Priority.High, False)
task2 = Task("Убраться дома", date(2026, 8, 25), "Пропылесосить и помыть пол", Priority.Medium, False)
task3 = Task("Позвонить другу", date(2026, 8, 20), "Обсудить встречу на выходных", Priority.Low, False)
task8 = RecurringTask("Выучить Python Recurring", date(2026, 8, 29), "Повторить Enum, циклы и функции", RepeatInterval.WEEKLY, Priority.High, False)
task9 = RecurringTask("Сделать проект Todo List", date(2026, 7, 29), "Добавить классы Task и список задач", RepeatInterval.WEEKLY, Priority.High, False)
task10 = RecurringTask("Прочитать книгу", date(2026, 8, 5), "Прочитать 50 страниц", RepeatInterval.WEEKLY, Priority.Medium, False)
task11 = RecurringTask("Спорт", date(2026, 8, 31), "Сделать тренировку 30 минут", RepeatInterval.WEEKLY, Priority.Low, False)

task_manager = TaskManager()

tasks = [task1, task2, task3, task8, task9, task10, task11] 
recurring_tasks = [task8, task9, task10, task11]

for task in tasks:
    task_manager.add_task(task)

for task in task_manager.get_all_tasks():
    print(task.title)

for task in task_manager.get_overdue_tasks():
    print(task.title, task.deadline)

task_manager.remove_task(task1)

print(f"{GREEN}=== Все задачи ==={RESET}")
for task in task_manager.get_all_tasks():
    print(task.title)

print(f"{GREEN}\n=== Завершение и переоткрытие задачи ==={RESET}")
print(f'{task8.title} done = {task8.done}, deadline = {task8.deadline}')
task_manager.complete_task(task8)
print(f'{task8.title} done = {task8.done}, deadline = {task8.deadline}')
task_manager.reopen_task(task8)
print(f'У {task8.title} done = {task8.done}, deadline = {task8.deadline}')

print(f"{GREEN}\n=== Повторное закрытие задачи ==={RESET}")
print(task10.title)
task_manager.complete_task(task10)
task_manager.complete_task(task10)

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

print(f"{GREEN}\nСледующие повторения:{RESET}")
for task in new_recurring_tasks:
    print(task.title, task.deadline, task.done)

print(f"{RED}\nПросроченные задачи:{RESET}")
found = False
for task in new_recurring_tasks:
    if task.is_overdue():
        print(task.title, task.deadline, task.done)
        found = True
if not found:
    print("There is no overdue tasks")
# todo.py

tasks = []

def add_task(task):
    if task.strip() == "":
        print("Error: Task cannot be empty.")
        return
    tasks.append(task)
    print(f"Added task: {task}")

def view_tasks():
    print("Your Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def delete_task(task_number):
    if 1 <= task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        print(f"Deleted task: {removed}")
    else:
        print("Error: Invalid task number.")

add_task("Finish Software Engin GitHub assignment")
add_task("Buy groceries")
view_tasks()
delete_task(1)
view_tasks()

# todo.py

tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Added task: {task}")

def view_tasks():
    print("Your Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

# Demo
add_task("Finish GitHub assignment")
add_task("Buy groceries")
view_tasks()

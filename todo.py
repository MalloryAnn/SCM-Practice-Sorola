# todo.py

tasks = []

def add_task(task):
    if task.strip() == "":
        print("Error: Task cannot be empty.")
        return
    tasks.append({"task": task, "done": False})
    print(f"Added task: {task}")

def view_tasks():
    print("Your Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else "✗"
        print(f"{i}. [{status}] {task['task']}")


def delete_task(task_number):
    if 1 <= task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        print(f"Deleted task: {removed}")
    else:
        print("Error: Invalid task number.")

def mark_done(task_number):
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        print(f"Marked task {task_number} as completed.")
    else:
        print("Error: Invalid task number.")

def clear_tasks():
    tasks.clear()
    print("All tasks cleared.")


add_task("Finish Software Engin GitHub assignment")
add_task("Buy groceries")
view_tasks()

mark_done(2)
view_tasks()

delete_task(1)
view_tasks()

clear_tasks()
view_tasks()


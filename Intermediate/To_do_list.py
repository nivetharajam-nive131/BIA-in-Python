tasks = []

def display_tasks():
    if len(tasks) == 0:
        print("No tasks to display.")
        return
    print("Here are your tasks:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")

def add_task():
    print("Enter a task:")
    task = input()
    tasks.append(task)
    print("Task added.")

def edit_task():
    display_tasks()
    print("Enter the number of the task you want to edit:")
    task_index = int(input()) - 1
    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task number.")
        return
    print("Enter the new task:")
    new_task = input()
    tasks[task_index] = new_task
    print("Task updated.")

def delete_task():
    display_tasks()
    print("Enter the number of the task you want to delete:")
    task_index = int(input()) - 1
    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task number.")
        return
    del tasks[task_index]
    print("Task deleted.")

while True:
    print("What would you like to do? (add/edit/delete/display/exit)")
    choice = input()
    if choice == "add":
        add_task()
    elif choice == "edit":
        edit_task()
    elif choice == "delete":
        delete_task()
    elif choice == "display":
        display_tasks()
    elif choice == "exit":
        break
    else:
        print("Invalid choice.")
'''
Sample Output:-
    What would you like to do? (add/edit/delete/display/exit)
    add
    Enter a task:
    breakfast
    Task added.
    What would you like to do? (add/edit/delete/display/exit)
    add
    Enter a task:
    interview
    Task added.
    What would you like to do? (add/edit/delete/display/exit)
    display
    Here are your tasks:
    1. breakfast
    2. interview
    What would you like to do? (add/edit/delete/display/exit)
    delete
    Here are your tasks:
    1. breakfast
    2. interview
    Enter the number of the task you want to delete:
    1
    Task deleted.
    What would you like to do? (add/edit/delete/display/exit)
    display
    Here are your tasks:
    1. interview
    What would you like to do? (add/edit/delete/display/exit)
    exit
'''
#========= TO-DO LIST =========
#1. View tasks
#2. Add a task
#3. Mark task as done
#4. Delete a task
#5. Save and Exit
#==============================

import os

Filename = "Text_File.txt"

#Loading tasks from file:
def load_tasks():
    tasks = []
    if os.path.exists(Filename):
        with open(Filename, 'r') as file:
            tasks = [line.strip() for line in file.readlines()]
    return tasks

#Saving tasks to file:
def save_tasks(tasks):
    with open(Filename, 'w') as file:
        for task in tasks:
            file.write(task + '\n')
    print("Tasks saved successfully!")  
#Viewing tasks:
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    print()
#Adding a task:
def add_task(tasks):
    task = input("Enter the task you want to add: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' added successfully!")
    else:
        print("Empty task cannot be added.")
    print()
#Marking a task as done:
def mark_task_done(tasks):

    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter the task number to mark as done: "))
            if 1 <= task_num <= len(tasks):
                done_task = tasks.pop(task_num - 1)
                print(f"Task '{done_task}' marked as done and removed from the list.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    print()
#Deleting a task:
def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter the task number to delete: "))
            if 1 <= task_num <= len(tasks):
                deleted_task = tasks.pop(task_num - 1)
                print(f"Task '{deleted_task}' deleted successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    print()
#Main program loop:
def main():
    tasks = load_tasks()
    while True:
        print("========= TO-DO LIST =========")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Mark task as done")
        print("4. Delete a task")
        print("5. Save and Exit")
        print("==============================")
        
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.\n")
if __name__ == "__main__":
    main()
#========= TO-DO LIST =========
#1. View tasks
#2. Add a task

#3. Mark task as done
#4. Delete a task
#5. Save and Exit
#==============================



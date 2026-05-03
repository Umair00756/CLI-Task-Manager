import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    
    try:
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print("Warning: Could not read the tasks file. Starting with an empty task list.")
        return []

def save_tasks(tasks):
    try:
        with open(TASKS_FILE, 'w') as f:
            json.dump(tasks, f, indent=4)
    except IOError:
        print("Error: Could not save tasks to file.")

def display_menu():
    print("\n--- Task Manager ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")
    print("--------------------")

def add_task(tasks):
    description = input("Enter the task description: ").strip()
    if description:
        new_task = {
            "description": description,
            "status": "pending"
        }
        tasks.append(new_task)
        save_tasks(tasks)
        print("Task added successfully.")
    else:
        print("Task description cannot be empty.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("\nCurrent Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = task.get("status", "pending")
        description = task.get("description", "No description")
        print(f"{index}. [{status.upper()}] {description}")

def mark_task_complete(tasks):
    if not tasks:
        print("No tasks to mark as complete.")
        return

    view_tasks(tasks)
    try:
        choice = int(input("\nEnter the task number to mark as complete: "))
        index = choice - 1
        
        if 0 <= index < len(tasks):
            tasks[index]["status"] = "completed"
            save_tasks(tasks)
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return

    view_tasks(tasks)
    try:
        choice = int(input("\nEnter the task number to delete: "))
        index = choice - 1
        
        if 0 <= index < len(tasks):
            deleted_task = tasks.pop(index)
            save_tasks(tasks)
            print(f"Task '{deleted_task['description']}' deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def main():
    tasks = load_tasks()

    while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

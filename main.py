
"""
Daily Task Manager
A simple command-line task manager using Python and JSON.
"""

import json
from datetime import datetime
from pathlib import Path

DATA_FILE = Path(__file__).with_name("tasks.json")


def load_tasks():
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (OSError, json.JSONDecodeError):
        print("Warning: Could not read task data.")
        return []


def save_tasks(tasks):
    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4)
    except OSError:
        print("Error: Tasks could not be saved.")


def add_task(tasks):
    title = input("Task title: ").strip()

    if not title:
        print("The title cannot be empty.")
        return

    description = input("Description: ").strip()
    due_date = input(
        "Due date (YYYY-MM-DD, or Enter to skip): "
    ).strip()

    if due_date:
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date. Use YYYY-MM-DD.")
            return

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")


def view_tasks(tasks):
    if not tasks:
        print("There are no tasks yet.")
        return

    print("\n--- YOUR TASKS ---")

    for number, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        due = task["due_date"] or "No due date"

        print(f"{number}. {task['title']} [{status}]")
        print(f"   Description: {task['description'] or 'None'}")
        print(f"   Due date: {due}")


def get_task_index(tasks, action):
    if not tasks:
        print(f"There are no tasks to {action}.")
        return None

    try:
        number = int(input(f"Task number to {action}: "))
    except ValueError:
        print("Please enter a whole number.")
        return None

    if number < 1 or number > len(tasks):
        print(f"Choose a number from 1 to {len(tasks)}.")
        return None

    return number - 1


def complete_task(tasks):
    index = get_task_index(tasks, "complete")

    if index is not None:
        tasks[index]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed.")


def delete_task(tasks):
    index = get_task_index(tasks, "delete")

    if index is not None:
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Deleted task: {removed['title']}")


def show_menu():
    print("\n===== DAILY TASK MANAGER =====")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Exit")


def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break

        else:
            print("Invalid choice. Select a number from 1 to 5.")


if __name__ == "__main__":
    main()

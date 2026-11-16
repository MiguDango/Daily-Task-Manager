# CS 26 Exam 2 – Python Program Technical Documentation

**Program:** Daily Task Manager  
**Student:** [Calalo, Miguel Agustin]  
**Course:** CS 26 – Software Development Fundamentals  
**Assessment:** Exam 2 – Python Program Technical Documentation (Weeks 4–5)

> **Testing note:** The results in Section J are simulated results obtained by running the program in an isolated test environment with prepared inputs. They are not claimed as tests personally performed in PyCharm. Run the same cases in your own PyCharm environment and update the results if your instructor requires personally observed results.

## A. Program Title and Overview

The **Daily Task Manager** is a command-line Python program designed for students and other users who need a simple way to organize everyday responsibilities. Users can add tasks with a title, description, and optional due date; view their tasks; mark tasks as completed; and delete tasks.

The program stores task information in a JSON file so that saved tasks can be loaded the next time the program runs. Its purpose is to make basic task organization easier while demonstrating Python programming concepts such as lists, tuples, dictionaries, functions, loops, conditional statements, file handling, and error handling.

## B. Problem Description

People may need to remember school assignments, household responsibilities, appointments, and personal activities. When these responsibilities are not organized, a person may overlook a task or forget its due date. The Daily Task Manager provides a simple way to record and review these responsibilities.

### Inputs

- A menu choice from 1 to 5.
- A task title.
- A task description.
- An optional due date in `YYYY-MM-DD` format.
- A task number when completing or deleting a task.

### Processing

- The program checks whether the title is empty.
- It validates a due date when one is entered.
- It stores each task as a dictionary in a list.
- It uses functions to add, display, complete, and delete tasks.
- It reads and writes task records in a JSON file.

### Outputs

- A numbered list of tasks.
- Each task's description, due date, and completion status.
- Confirmation messages when tasks are added, completed, or deleted.
- Error messages when the user enters invalid information.
- A JSON file containing saved task records.

## C. Program Objectives

1. Allow users to add a task with a title, description, and optional due date.
2. Display saved tasks with their current completion status.
3. Allow users to mark a selected task as completed.
4. Allow users to delete a selected task.
5. Save and load task records using a JSON file so that records persist between program runs.

## D. Program Requirements and Features

### Requirements

- Python 3.8 or newer.
- A Python editor or IDE, such as PyCharm.
- No external Python packages are required.

### Implemented features

- Add a task.
- View all saved tasks.
- Mark a task as completed.
- Delete a task.
- Save and load tasks using JSON.
- Reject an empty title.
- Check the date format when a due date is supplied.
- Reject invalid menu choices and invalid task numbers.

### Assumptions and limitations

- The program is operated through a text-based menu.
- The due date is optional and must use `YYYY-MM-DD` when supplied.
- The program is designed for a single local task list stored in `tasks.json`.
- It does not currently provide user accounts, reminders, calendar synchronization, or a graphical interface.
- If the JSON file is malformed, the program displays a warning and starts with an empty in-memory task list. It does not automatically repair the damaged file.

## E. Program Structure and Modules

### File structure

```text
Daily-Task-Manager/
├── main.py
├── tasks.json
├── README.md
├── pseudocode.txt
├── TEST_CASES.md
└── .gitignore
```

| File | Purpose |
|---|---|
| `main.py` | Contains the program's menu, functions, validation, and task operations. |
| `tasks.json` | Stores task records in JSON format. It begins as an empty list (`[]`). |
| `README.md` | Explains the project, features, requirements, and how to run it. |
| `pseudocode.txt` | Describes the program's main logic in pseudocode. |
| `TEST_CASES.md` | Holds test scenarios and their results. |
| `.gitignore` | Excludes Python cache files from Git tracking. |

### Modules and imports

The project currently has one user-created Python source file, `main.py`. It imports three modules from Python's standard library:

```python
import json
from datetime import datetime
from pathlib import Path
```

- `json` reads and writes task data in JSON format.
- `datetime` checks whether an entered due date matches the required date format.
- `Path` builds the path to `tasks.json` relative to `main.py` and checks whether the file exists.

These are standard-library imports, not separate custom modules written for this project. The current version is organized into functions within `main.py`; it does not yet split the program into multiple user-created `.py` modules.

## F. Data Structures

The program uses a list and dictionaries to manage task records. The updated version also uses a tuple for the fixed menu options.

### 1. List

```python
tasks = load_tasks()
```

The `tasks` variable contains the collection of task records. A list is appropriate because users can add tasks, remove tasks, and view multiple records. The list can change while the program is running.

### 2. Tuple

```python
MENU_OPTIONS = (
    "Add a task",
    "View tasks",
    "Mark a task as completed",
    "Delete a task",
    "Exit",
)
```

A tuple stores the five menu labels. A tuple is appropriate because these menu options are fixed in this version of the program and do not need to be changed during normal use. Unlike a list, a tuple is immutable.

### 3. Dictionary

```python
task = {
    "title": title,
    "description": description,
    "due_date": due_date,
    "completed": False,
}
```

Each task is stored as a dictionary containing related information under named keys. A dictionary is appropriate because the program can access a task's title, description, due date, and completion status by key.

## G. Functions

The program is divided into functions so that each operation has a clear responsibility.

| Function | Parameters | Return value | Purpose |
|---|---|---|---|
| `load_tasks()` | None | A list of tasks, or an empty list | Reads saved task data from JSON. |
| `save_tasks(tasks)` | `tasks` | None | Writes the task list to the JSON file. |
| `add_task(tasks)` | `tasks` | None | Gets task details, validates them, and adds a task. |
| `view_tasks(tasks)` | `tasks` | None | Displays tasks and their status. |
| `get_task_index(tasks, action)` | `tasks`, `action` | An index or `None` | Gets and validates a task number. |
| `complete_task(tasks)` | `tasks` | None | Marks the selected task as completed. |
| `delete_task(tasks)` | `tasks` | None | Removes the selected task. |
| `show_menu()` | None | None | Displays the menu options. |
| `main()` | None | None | Loads tasks and controls the main menu loop. |

### Code excerpt 1: Adding a task

```python
task = {
    "title": title,
    "description": description,
    "due_date": due_date,
    "completed": False,
}

tasks.append(task)
save_tasks(tasks)
```

This excerpt creates a dictionary for a new task. The task is appended to the list, then `save_tasks()` writes the updated list to the JSON file. The `completed` value begins as `False`, meaning the task is pending.

### Code excerpt 2: Validating a task number

```python
try:
    number = int(input(f"Task number to {action}: "))
except ValueError:
    print("Please enter a whole number.")
    return None

if number < 1 or number > len(tasks):
    print(f"Choose a number from 1 to {len(tasks)}.")
    return None

return number - 1
```

The program converts the user's entry into an integer. If the entry cannot be converted, `ValueError` is handled. It then checks whether the number is within the available task range. The function returns a zero-based list index when the number is valid.

## H. File Handling

The program uses `tasks.json` as its data file. JSON is a text-based format that can represent lists and dictionaries.

### Reading a file

```python
with DATA_FILE.open("r", encoding="utf-8") as file:
    data = json.load(file)
```

The `"r"` mode opens the file for reading. `json.load()` converts the JSON content into Python data.

### Writing a file

```python
with DATA_FILE.open("w", encoding="utf-8") as file:
    json.dump(tasks, file, indent=4)
```

The `"w"` mode opens the file for writing. `json.dump()` writes the task list as JSON. This replaces the file's previous contents with the current task data.

### Purpose of `with`

The `with` statement manages the file context and closes the file after the indented block finishes, including when an exception occurs during the operation.

### Missing or malformed files

- If `tasks.json` does not exist, `load_tasks()` returns an empty list.
- If the file contains invalid JSON or cannot be read, the program catches `json.JSONDecodeError` or `OSError`, displays a warning, and returns an empty list.
- If the JSON value is not a list, the program returns an empty list.
- If saving fails because of a file-related error, `save_tasks()` displays an error message.

Task records persist between runs when the JSON file is successfully saved.

## I. Error Handling

The program uses input validation and `try`/`except` blocks to handle expected problems.

| Situation | Handling |
|---|---|
| Empty task title | Displays a message and does not add the task. |
| Incorrect due-date format | Catches `ValueError` and asks for `YYYY-MM-DD`. |
| Non-numeric task number | Catches `ValueError` and asks for a whole number. |
| Task number outside the available range | Displays the valid range and does not change a task. |
| Missing, unreadable, or malformed JSON file | Handles file or JSON errors and returns an empty list. |
| File cannot be saved | Catches `OSError` and displays an error message. |
| Invalid menu choice | Displays a message and returns to the menu. |

Input-validation errors arise from data that is entered in a manner inconsistent with the program's requirements, or from data that lies outside of the allowable range. Exceptions pertaining to files are processed independently. The current program does not have a general exception processor for every type of program error (there is no code for this); it is possible that some program errors are not caught and must be investigated.

## J. Testing, Debugging, and Results

### Test cases

| Test ID | Scenario | Input / Action | Expected result | Simulated actual result | Status |
|---|---|---|---|---|---|
| TC01 | Normal case: add and view a task | Add `Study Python`, description `Review loops`, due date `2026-11-20`, then view tasks | Task is saved and displayed as Pending | Program displayed “Task added successfully” and showed the task as Pending | PASS |
| TC02 | Boundary case: task number below range | Add one task, then enter `0` when asked which task to complete | Program rejects the number and displays the valid range | Program displayed “Choose a number from 1 to 1.” | PASS |
| TC03 | Invalid menu input | Enter `hello` at the main menu | Program displays an invalid-choice message and continues | Program displayed “Invalid choice. Select a number from 1 to 5.” | PASS |
| TC04 | Invalid date format | Enter `20-11-2026` as the due date | Program rejects the date and does not add the task | Program displayed “Invalid date. Use YYYY-MM-DD.” and did not save the task | PASS |
| TC05 | File persistence | Add a task, exit, start the program again, and view tasks | Previously saved task is displayed after restarting | The task `Read chapter` appeared after the second program run | PASS |

### Debugging and verification

No defect in the program was seen in these five simulated scenarios. Verification was done to ensure that the program received correct task information, that invalid task data was rejected, that the range of task numbers was adhered to, and that saved data was retained between different runs of the program. These scenarios were found to have the expected program messages and task-file changes in their test results.

This verification does not guarantee that all possible input or file conditions are not faulty. Further testing may take place.

## K. Conclusion

The Daily Task Manager is a command line version of basic task organization. It enables to add, view, complete and delete tasks, and also save records between runs, using JSON. The project is an example of lists, tuples, dictionaries, functions, loops, conditional statements, file handling, and error handling.

The current disadvantages of it are that it doesn't have a GUI, users, reminders, or multi-user storage. Possible future improvements include adding task priorities, search and filtering, and a graphical user interface.

## L. References

- CS 26 – Software Development Fundamentals, *Exam 2: Python Program Technical Documentation (Weeks 4–5)*, student instructions provided for this assessment.
- Python Software Foundation, *Python Documentation*: https://docs.python.org/3/
- Python Software Foundation, *json — JSON encoder and decoder*: https://docs.python.org/3/library/json.html

**Acknowledgment:** AI assistance was used to help with proper grammar and revisions.
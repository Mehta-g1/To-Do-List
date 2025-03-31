# Task Manager

A simple Python-based task manager that allows users to add, view, delete, save, and load tasks.

## Features
- **Add Task**: Add new tasks to your task list.
- **View Tasks**: Display all saved tasks.
- **Delete Task**: Remove a specific task by its number.
- **Save Tasks**: Save tasks to a file (`TaskList.txt`) for future use.
- **Load Tasks**: Automatically load saved tasks when the program starts.

## Functions Overview

### `AddTask()`
- Prompts the user to enter a task.
- Adds the task to the `tasklist` list.
- Displays a success message.

### `ViewTask()`
- Displays the list of tasks.
- If the list is empty, it shows a message indicating no tasks are available.

### `DeleteTask()`
- Calls `ViewTask()` to display tasks.
- Asks the user to enter the task number to delete.
- Deletes the specified task and updates the list.
- Handles invalid inputs gracefully.

### `SaveTask()`
- Writes all tasks to `TaskList.txt` file.
- Displays a success message after saving.
- Handles cases where there are no tasks to save.

### `Loadtask()`
- Reads tasks from `TaskList.txt` (if available).
- Loads the tasks into `tasklist` when the program starts.
- Displays a message indicating tasks were loaded.

## How to Use

### 1. Clone the Repository
```sh
git clone https://github.com/your-username/task-manager.git
cd task-manager
2. Run the Script
sh
Copy
Edit
python task_manager.py
3. Use the Menu Options
After running the script, you will see the following menu:

markdown
Copy
Edit
1. Add Task
2. View Task
3. Delete Task
4. Save & Load Task
5. Exit
Press 1 to add a task.

Press 2 to view tasks.

Press 3 to delete a task.

Press 4 to manually save tasks.

Press 5 to save and exit the program.

Notes
The program automatically loads saved tasks when it starts.

Tasks are saved in TaskList.txt.

If the file is missing, it will create a new one when saving.

License
This project is open-source. Feel free to modify and use it as needed.

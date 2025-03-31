# Command-Line To-Do List Application

## Description
This is a simple command-line To-Do List application that allows users to manage their daily tasks efficiently. 
The application provides options to add, view, delete, save, and load tasks from a file.

## Features
- **Add Tasks**: Users can add new tasks to the list.
- **View Tasks**: Displays all the current tasks.
- **Delete Tasks**: Users can remove completed or unnecessary tasks.
- **Save Tasks**: Saves tasks to a text file for future use.
- **Load Tasks**: Loads previously saved tasks from a file.
- **Error Handling**: Handles invalid user inputs and file operations gracefully.

## Technical Requirements
- **File Handling**: Uses Python’s file I/O operations to read and write task data.
- **Data Structure**: Stores tasks in a list.
- **User Interface**: Simple text-based interface.
- **Cross-Platform Compatibility**: Works on Windows, macOS, and Linux.

## Prerequisites
- Python installed on your system.

## Usage
1. Select an option from the menu:
   - Press `1` to add a task.
   - Press `2` to view tasks.
   - Press `3` to delete a task.
   - Press `4` to save tasks to a file.
   - Press `5` to exit.
2. Follow the prompts to manage tasks effectively.

## File Storage
- Tasks are saved in `TaskList.txt`.
- When loading, the application reads from `TaskList.txt` and restores the task list.

## Error Handling
- Prevents invalid input types.
- Ensures the application doesn’t crash due to missing files.
- Checks for empty task lists before performing operations.

## Author
- **Vikash Kumar Mehta**  
- GitHub: [Vikash Kumar Mehta](https://github.com/mehta-g1)

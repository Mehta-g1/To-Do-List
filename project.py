import os

# List to store tasks
tasklist = []

def AddTask():
    """Adds a new task to the task list."""
    task = input("Enter Your Task:")
    tasklist.append(task)
    print("Task Added Successfully!")

def ViewTask():
    """Displays all tasks in the task list."""
    i = 1
    if len(tasklist) > 0:
        print("\n\t--- Task List ---")
        for e in tasklist:
            print(i, ".  ", e, sep='')
            i += 1
        return True
    else:
        print("Task list is Empty!")
        return False

def DeleteTask():
    """Deletes a task from the task list based on user input."""
    if not ViewTask():
        return  # Exit if task list is empty
    try:
        t_no = int(input("\nEnter Task Number to delete:"))
        del tasklist[t_no - 1]  # Remove the task by index
        print("Task Deleted Successfully!\n")
        ViewTask()
    except ValueError:
        print("Task Number should be an integer!")
    except IndexError:
        print("Task Number is Invalid!")
    except Exception:
        print("Unknown Exception from DeleteTask()")

def SaveTask():
    """Saves tasks to a file."""
    try:
        file = open("TaskList.txt", "w")
        i = 0
        temp = tasklist[-1]  # Get the last task
        tasklist[-1] = temp + " "  # Ensure spacing for the last task
        for e in tasklist:
            file.write(e + "\n")
            i += 1
        print(i, "Task(s) saved into file successfully!")
        file.close()
    except IndexError:
        print("Nothing to save into file")
    except Exception:
        print("Unknown Exception from SaveTask()")

def Loadtask():
    """Loads tasks from a file."""
    try:
        file = open("TaskList.txt", "r")
        i = 1
        tasklist.clear()  # Clear current tasks before loading
        for e in file.readlines():
            tasklist.append(e.strip())  # Remove newline characters
            i += 1
        file.close()
        print(i, "task(s) loaded from file")
    except FileNotFoundError:
        print("Nothing to do Today!")
    except Exception:
        print("Unknown Exception from LoadTask()")

# Try loading tasks at the beginning
try:
    Loadtask()
except FileNotFoundError:
    pass

while True:
    os.system("cls")  # Clear the screen (works on Windows)
    print("1.\tAdd task")
    print("2.\tView Task")
    print("3.\tDelete Task")
    print("4.\tSave & Load Task")
    print("5.\tExit")

    choice = input("Enter Your Choice (Int): ")

    match choice:
        case "1":
            AddTask()
            input("\n\tPress Enter for HOME")
        case "2":
            ViewTask()
            input("\n\tPress Enter for HOME")
        case "3":
            DeleteTask()
            input("\n\tPress Enter for HOME")
        case "4":
            SaveTask()
            input("\n\tPress Enter for HOME")
        case "5":
            SaveTask()  # Save before exiting
            input("\n\tPress Enter for Exit")
            exit()
        case _:
            print("Invalid choice! Please enter a valid number.")
            input("\n\tPress Enter for Home")

import re
from datetime import datetime

todo_list = {}

def is_valid_date(date_str):
    if not re.match(r'^\d{4}-\d{2}-\d{2}$', date_str):
        print("Invalid date format. Please use YYYY-MM-DD.")
        return False
    
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d").date()  # Convert to datetime.date
        if date < datetime.now().date():  # Ensure comparison is with date
            print("You cannot enter a past date.")
            return False
    except ValueError:
        print("Invalid date. Please enter a valid date.")
        return False

    return True

def add_task():
    task = input("Enter the task to add: ")
    while True:
        date = input("Enter the date (YYYY-MM-DD): ")
        if not is_valid_date(date):
            continue  # Continue loop if date is invalid
        
        if date in todo_list:
            todo_list[date].append(task)
        else:
            todo_list[date] = [task]
        print(f"Task '{task}' added for {date}.")
        break  # Exit loop after successful addition

def remove_task():
    while True:
        date = input("Enter the date (YYYY-MM-DD): ")
        if not is_valid_date(date):
            continue 
        
        if date not in todo_list or not todo_list[date]:
            print(f"No tasks found for {date}. The to-do list is empty for this date.")
            continue  # Ask for date again if no tasks are found
        
        print(f"Tasks for {date}:")
        for idx, item in enumerate(todo_list[date], 1):
            print(f"{idx}. {item}")

        while True:
            try:
                task_index = int(input("Enter the number of the task to remove: ")) - 1
                if 0 <= task_index < len(todo_list[date]):
                    task_to_remove = todo_list[date][task_index]
                    todo_list[date].remove(task_to_remove)
                    if not todo_list[date]:
                        del todo_list[date]
                    print(f"Task '{task_to_remove}' removed from {date}.")
                    break  # Exit inner loop after successful removal
                else:
                    print("Invalid task number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        break  # Exit outer loop after task removal

def view_tasks(date=None):
    if date:
        if date in todo_list and todo_list[date]:
            print(f"Tasks for {date}:")
            for item in todo_list[date]:
                print(f"- {item} - Pending")
        else:
            print(f"No tasks found for {date}.")
    else:
        if not todo_list:
            print("No tasks in the list.")
        else:
            for date, tasks in todo_list.items():
                print(f"Tasks for {date}:")
                for item in tasks:
                    print(f"- {item} - Pending")

def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            if not todo_list:
                print("The to-do list is empty. You cannot remove a task.")
            else:
                remove_task()
        elif choice == '3':
            date = input("Enter the date to view tasks for (YYYY-MM-DD) or leave blank to view all tasks: ")
            view_tasks(date)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

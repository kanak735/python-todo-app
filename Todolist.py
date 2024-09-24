import os

# File to store the tasks
TASKS_FILE = 'tasks.txt'

def load_tasks():
    """Load tasks from the file."""
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            for line in file:
                task, status = line.strip().split(' | ')
                tasks.append({"task": task, "status": status})
    return tasks

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(f"{task['task']} | {task['status']}\n")

def display_tasks(tasks):
    """Display the list of tasks."""
    if not tasks:
        print("\nNo tasks available!")
    else:
        print("\nCurrent Tasks:")
        for i, task in enumerate(tasks):
            status = "✔" if task['status'] == "completed" else "✘"
            print(f"{i + 1}. {task['task']} [{status}]")

def add_task(tasks):
    """Add a new task to the list."""
    task_name = input("Enter the task: ")
    tasks.append({"task": task_name, "status": "pending"})
    save_tasks(tasks)
    print(f"Task '{task_name}' added!")

def mark_task_complete(tasks):
    """Mark a task as complete."""
    display_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to mark complete: "))
        if tasks[task_num - 1]['status'] == "completed":
            print("Task is already completed!")
        else:
            tasks[task_num - 1]['status'] = "completed"
            save_tasks(tasks)
            print(f"Task '{tasks[task_num - 1]['task']}' marked as completed!")
    except (IndexError, ValueError):
        print("Invalid task number.")

def remove_task(tasks):
    """Remove a task from the list."""
    display_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to remove: "))
        removed_task = tasks.pop(task_num - 1)
        save_tasks(tasks)
        print(f"Task '{removed_task['task']}' removed!")
    except (IndexError, ValueError):
        print("Invalid task number.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Menu:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as complete")
        print("4. Remove task")
        print("5. Exit")
        
        choice = input("Enter your choice (1/2/3/4/5): ")
        
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            print("Exiting the To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

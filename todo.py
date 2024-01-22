import datetime

# Dictionary to store tasks
tasks = {}

def add_task():
    task_name = input("Enter task name: ")
    category = input("Enter task category: ")
    deadline_str = input("Enter task deadline (YYYY-MM-DD): ")
    deadline = datetime.datetime.strptime(deadline_str, '%Y-%m-%d').date() if deadline_str else None
    priority = int(input("Enter task priority (1 - Low, 2 - Medium, 3 - High): "))
    label = input("Enter task label: ")

    tasks[task_name] = {
        'category': category,
        'deadline': deadline,
        'priority': priority,
        'label': label,
        'status': 'Not Started'
    }

def view_tasks():
    print("\nTask List:")
    for task_name, task_details in tasks.items():
        print(f"Task: {task_name}")
        print(f"  Category: {task_details['category']}")
        print(f"  Deadline: {task_details['deadline']}")
        print(f"  Priority: {task_details['priority']}")
        print(f"  Label: {task_details['label']}")
        print(f"  Status: {task_details['status']}")
        print()

def prioritize_tasks():
    sorted_tasks = sorted(tasks.items(), key=lambda x: (x[1]['priority'], x[1]['deadline']))
    tasks.clear()
    tasks.update(sorted_tasks)

def monitor_progress():
    completed_tasks = sum(1 for task in tasks.values() if task['status'] == 'Completed')
    total_tasks = len(tasks)

    print("\nTask Progress:")
    print(f"Completed Tasks: {completed_tasks}")
    print(f"Total Tasks: {total_tasks}")
    print(f"Progress: {completed_tasks}/{total_tasks} tasks completed ({(completed_tasks / total_tasks) * 100:.2f}%)")

# Main loop
while True:
    print("\n==== To-Do List Manager ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Prioritize Tasks")
    print("4. Monitor Progress")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        prioritize_tasks()
        print("Tasks prioritized.")
    elif choice == '4':
        monitor_progress()
    elif choice == '5':
        print("Exiting To-Do List Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

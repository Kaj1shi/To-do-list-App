import datetime

# Each task is a dictionary: text, timestamp, status
tasks = []

# Display menu
def show_menu():
    print("\n=== TO-DO LIST MENU ===")
    print("1. View All Tasks")
    print("2. View Done Tasks")
    print("3. View Not Done Tasks")
    print("4. Add Task")
    print("5. Delete Task")
    print("6. Mark Task as Done")
    print("7. Exit")

# Display a list of tasks based on status
def view_tasks(filter_by=None):
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks:")
    count = 0
    for i, task in enumerate(tasks, start=1):
        if filter_by == "done" and not task['done']:
            continue
        if filter_by == "not_done" and task['done']:
            continue

        status = "✅ Done" if task['done'] else "❌ Not Done"
        print(f"{i}. {task['text']} ({status}, added on {task['timestamp']})")
        count += 1

    if count == 0:
        print("No matching tasks found.")

# Add a new task
def add_task():
    task_text = input("Enter task: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tasks.append({'text': task_text, 'timestamp': timestamp, 'done': False})
    print(f"Task '{task_text}' added.")

# Delete a task
def delete_task():
    view_tasks()
    if tasks:
        try:
            index = int(input("Enter task number to delete: "))
            if 1 <= index <= len(tasks):
                removed = tasks.pop(index - 1)
                print(f"Task '{removed['text']}' deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a number.")

# Mark a task as done
def mark_task_done():
    view_tasks(filter_by="not_done")
    if tasks:
        try:
            index = int(input("Enter task number to mark as done: "))
            if 1 <= index <= len(tasks):
                tasks[index - 1]['done'] = True
                print(f"Task '{tasks[index - 1]['text']}' marked as done.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a number.")

# Main program loop
def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-7): ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            view_tasks(filter_by="done")
        elif choice == '3':
            view_tasks(filter_by="not_done")
        elif choice == '4':
            add_task()
        elif choice == '5':
            delete_task()
        elif choice == '6':
            mark_task_done()
        elif choice == '7':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Run the app
if __name__ == "__main__":
    main()

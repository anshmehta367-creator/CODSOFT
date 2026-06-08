# A simple CLI To-Do List Application in Python

def display_menu():
    print("\n" + "="*25)
    print("      TO-DO LIST")
    print("="*25)
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")
    print("="*25)

def main():
    # Initialize an empty list to store tasks
    tasks = []

    while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()

        # 1. View Tasks
        if choice == '1':
            if not tasks:
                print("\nYour to-do list is empty!")
            else:
                print("\nYOUR TASKS:")
                for index, task in enumerate(tasks, 1):
                    # Show a checkmark for completed tasks, otherwise a blank space
                    status = "✓" if task['completed'] else " "
                    print(f"{index}. [{status}] {task['text']}")

        # 2. Add Task
        elif choice == '2':
            task_text = input("\nEnter the task name: ").strip()
            if task_text:
                # Store each task as a dictionary with text and a completion status
                tasks.append({'text': task_text, 'completed': False})
                print(f"Task '{task_text}' added successfully.")
            else:
                print("Task cannot be empty.")

        # 3. Mark Task as Complete
        elif choice == '3':
            if not tasks:
                print("\nNo tasks to mark complete.")
                continue
            
            try:
                task_num = int(input("\nEnter the task number to complete: "))
                if 1 <= task_num <= len(tasks):
                    tasks[task_num - 1]['completed'] = True
                    print(f"Task {task_num} marked as complete!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        # 4. Delete Task
        elif choice == '4':
            if not tasks:
                print("\nNo tasks to delete.")
                continue

            try:
                task_num = int(input("\nEnter the task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    print(f"Removed task: '{removed_task['text']}'")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        # 5. Exit
        elif choice == '5':
            print("\nGoodbye! Stay productive!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()

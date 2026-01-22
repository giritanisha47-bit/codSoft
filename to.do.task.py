tasks = []

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(i, task)

    elif choice == "3":
        num = int(input("Enter task number to update: "))
        new_task = input("Enter new task: ")
        tasks[num - 1] = new_task
        print("Task updated!")

    elif choice == "4":
        num = int(input("Enter task number to delete: "))
        tasks.pop(num - 1)
        print("Task deleted!")

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")

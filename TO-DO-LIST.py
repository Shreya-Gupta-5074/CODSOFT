tasks = {}

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Mark as Done")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        title = input("Task name: ")
        tasks[title] = "Pending"
        print("Task added!")

    elif choice == "2":
        if not tasks:
            print("No tasks found.")
        else:
            for t, status in tasks.items():
                print(f"{t} → {status}")

    elif choice == "3":
        title = input("Enter task name to mark done: ")
        if title in tasks:
            tasks[title] = "Completed"
            print("Task updated!")
        else:
            print("Task not found!")

    elif choice == "4":
        break
    else:
        print("Invalid choice!")

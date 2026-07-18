# ---------- Load tasks from the file ----------
try:
    with open("tasks.txt", "r") as file:
        tasks = file.read().splitlines()
except FileNotFoundError:
    tasks = []


# ---------- Main program ----------
while True:

    print("\n...........Welcome...........")
    print("..........To-Do-List..........")
    print("Type 1 to View List.")
    print("Type 2 to Add a Task.")
    print("Type 3 to Remove a Task.")
    print("Type 0 to Exit.")

    choice = input("Type your chosen option here: ")

    # View tasks
    if choice == "1":
        if not tasks:
            print("You haven't added any tasks.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    # Add task
    elif choice == "2":
        task = input("Enter a task: ")
        tasks.append(task)

        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(task + "\n")

        print("Task added!")

    # Remove task
    elif choice == "3":
        if not tasks:
            print("You have no tasks to remove.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            try:
                num = int(input("Enter task number to remove: "))

                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)

                    with open("tasks.txt", "w") as file:
                        for task in tasks:
                            file.write(task + "\n")

                    print(f"Removed: {removed}")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    # Exit
    elif choice == "0":
        print("Goodbye!")
        break

    # Invalid option
    else:
        print("Invalid choice. Please try again.")
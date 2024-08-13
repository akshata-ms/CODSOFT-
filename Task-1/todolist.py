def display_menu():
    print("\n|| To-Do List Menu ||")
    print("1. Add a task")
    print("2. Show all tasks")
    print("3. Mark task as done")
    print("4. Exit")

def add_task(tasks):
    n_tasks = int(input("\nEnter the number of tasks you want to add: "))
    for i in range(n_tasks):
        task = input(f"Task {i+1}: ")
        tasks.append({"task": task, "done": False})
        print("Task added successfully!")

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks in the to-do list.")
    else:
        print("\nTasks:")
        for index, task in enumerate(tasks, start=1):
            status = "Done" if task["done"] else "Not Done"
            print(f"{index}. {task['task']} - {status}")

def mark_task_done(tasks):
    if not tasks:
        print("\nNo tasks to mark as done.")
        return

    try:
        task_index = int(input("\nEnter the task number to mark as done: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []

    while True:
        display_menu()
        choice = input("\nSelect your option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            print("Exiting the To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()





        


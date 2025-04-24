todo_list = []

def show_menu():
    print("\nTo-Do List Menu")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks():
    try:
        with open("/Users/saismital/Documents/Saismita/Study/AIML/Python/to-do_list.txt","r") as file:
            content = file.read();
        if content == "":
            print("Your to-do list is empty! Please add tasks to view")
        else:
            print("\nYour Tasks:")
            print(content)
    except FileNotFoundError:
            print("File not found.")
        

def add_task():
    task = input("Enter a new task: ")
    todo_list.append(task)
    with open("/Users/saismital/Documents/Saismita/Study/AIML/Python/to-do_list.txt","w") as file:
        for index, item in enumerate(todo_list, start=1):
            file.write(f"{index}. {item}\n")
    print("Task added!")

def remove_task():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 0 < task_num <= len(todo_list):
            removed = todo_list.pop(task_num - 1)
            with open("/Users/saismital/Documents/Saismita/Study/AIML/Python/to-do_list.txt","w") as file:
                file.writelines(todo_list)
            print(f"Task '{removed}' removed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Goodbye! 👋")
        break
    else:
        print("Invalid choice. Try again.")

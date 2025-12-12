list_task = []

try:
    file = open("todos.txt", "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        list_task.append(line.strip())

except FileNotFoundError:
    pass

print("=== To-Do List ===")
while True:
    user_option = input("\n1. Add task \n2. View tasks \n3. Complete task \n4. Quit \nChoose an option: ")

    if user_option == "1":
        task = input("\nEnter a new task: ")
        list_task.append(task)
        # Save to file
        file = open("todos.txt", "w")
        for task in list_task:
            file.write(task + "\n")
        file.close()
        print("Task added!")

    elif user_option == "2":
        print(f"\nYour tasks:")
        if len(list_task) == 0:
            print("You currently don't have any tasks!")
        else:
            task_num = 0
            for t in list_task:
                task_num += 1
                print(f"{task_num}. {t}")

    elif user_option == "3":
        task_complete = int(input("Enter task number to complete: "))
        task_complete -= 1
        list_task.remove(list_task[task_complete])
        # Save to file
        file = open("todos.txt", "w")
        for task in list_task:
            file.write(task + "\n")
        file.close()
        print("Task completed!")

    elif user_option == "4":
        break

    else:
        print("Invalid entry try again.")
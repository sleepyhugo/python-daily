shopping_list = []

while True:
    user_option = int(input("What would you like to do today? \n1. Add an item \n2. Remove an item \n3. Show shopping list \n4. Exit \n"))

    if user_option == 1:
        item = input("Enter the item you want to add: ")
        shopping_list.append(item)
        print(item + " added.")

    elif user_option == 2:
        item_remove = input("Enter the name of the item you want to remove: ")

        if item_remove in shopping_list:
            shopping_list.remove(item_remove)
            print(item_remove + " has been removed.")
        else:
            print("Item not found.")

    elif user_option == 3:
        if len(shopping_list) == 0:
            print("Shopping list is empty.")
        else:
            print("Your shopping list:")
            for item in shopping_list:
                print("- " + item)

    elif user_option == 4:
        print("Goodbye!")
        break

    else:
        print("Choose an option from 1-4.")

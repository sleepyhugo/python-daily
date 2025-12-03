import random

print("Welcome!")

while True:
    random_number = random.randint(1, 6)

    print(f"You rolled: {random_number}")

    while True:
        again = input("Roll again? (y/n): ").lower()

        if again == "y" or again == "n":
            break
        else:
            print("Invalid choice.")
    if again == "n":
        break
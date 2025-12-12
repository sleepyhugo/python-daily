import random

print("=== Password Generator ===")
possible_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~!@#$%^&*"

while True:
    password = ""
    user_input = int(input("Enter password length: "))
    for i in range(user_input):
        random_character = random.choice(possible_characters)
        password += random_character

    print(password)

    another = input("\nGenerate another? (y/n): ")
    if another.lower() != "y":
        print("Goodbye!")
        break

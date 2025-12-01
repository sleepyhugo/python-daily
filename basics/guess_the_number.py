secret_num = 9
guess = int(input("Guess the secret number: "))

while guess != secret_num:

    if guess > secret_num:
        print("Guess is too high! Try Again!")
    else:
        print("Guess is too low! Try Again!")

    guess = int(input("Guess the secret number: "))

print("Correct!")

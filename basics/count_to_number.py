number = int(input("Enter a positive number: "))

if number > 0:
    for i in range(1, number + 1):
        print(i)
elif number <= 0:
    print("Number entered must be positive!")
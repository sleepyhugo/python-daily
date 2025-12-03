num_list = []
total = 0
count = 0
average = 0.0

while True:
    try:
        user_input = input("Enter a number (or 'done' to finish): ")

        if user_input == "done":
            break
        else:
            num = float(user_input)
            num_list.append(num)
            total += num
            count += 1

    except:
        print("Invalid input, try again")
        continue

if len(num_list) == 0:
    print("No numbers were entered.")
else:
    print(num_list)
    average = total / count

    print(f"Total: {total}")
    print(f"Count: {count}")
    print(f"Average: {average}")
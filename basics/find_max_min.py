
num_list = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    num_list.append(num)

max_value = num_list[0]
min_value = num_list[0]

for num in num_list:
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num

print(f"Largest: {max_value}")
print(f"Smallest: {min_value}")

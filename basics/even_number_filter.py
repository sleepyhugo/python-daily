numbers = input("Enter a list of numbers: ")

list_nums = []

for nums in numbers.split():
    number = int(nums)
    list_nums.append(number)  # allow duplicates

def filter_even_numbers(numbers):
    even_list = []
    for n in numbers:
        if n % 2 == 0:
            even_list.append(n)
    return even_list

print(filter_even_numbers(list_nums))

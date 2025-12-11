def binary_search(numbers, target):
    # Returns the index of target in numbers, or -1 if not found.
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2
        guess = numbers[mid]

        if guess == target:
            return mid
        elif guess < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Demo
if __name__ == "__main__":
    nums = [1, 3, 5, 7, 9, 11]
    target = 7

    result = binary_search(nums, target)

    if result != -1:
        print(f"Found {target} at index {result}")
    else:
        print(f"{target} not found.")

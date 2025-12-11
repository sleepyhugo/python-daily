def linear_search(items, target):
    #Return the index of target by checking each item one-by-one.
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1


# Demo
if __name__ == "__main__":
    data = [4, 8, 15, 16, 23, 42]
    target = 15

    result = linear_search(data, target)

    if result != -1:
        print(f"Found {target} at index {result}")
    else:
        print(f"{target} not found.")

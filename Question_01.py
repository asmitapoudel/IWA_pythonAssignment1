# Write a Python function to find the Max of three numbers


def find_max(numbers):
    return max(numbers)


input_number = [int(x) for x in input("Enter numbers ").split()]
print(find_max(input_number))

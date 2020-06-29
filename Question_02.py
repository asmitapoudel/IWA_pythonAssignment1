# Write a Python function to sum all the numbers in a list.
def find_sum(numbers):
    return sum(numbers)


input_number = [int(x) for x in input("Enter numbers ").split()]
print(find_sum(input_number))
# Write a Python function to multiply all the numbers in a list.
def find_mul(numbers):
    result = 1
    for i in numbers:
        result *= i
    return result


input_number = [int(x) for x in input("Enter numbers ").split()]
print(find_mul(input_number))
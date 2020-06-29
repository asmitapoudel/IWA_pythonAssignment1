# Write a Python program to create a function that takes one argument, and that argument
# will be multiplied with an unknown given number.


def find_mul(num):
    return lambda x: x * num


result = find_mul(2)
print("Multiply by 2", result(5))
result = find_mul(5)
print("Multiply by 5", result(5))

#  Write a Python function to calculate the factorial of a number (a non-negative integer).
#  The function accepts the number as an argument.


def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)


num = int(input('Enter number '))
print(f'Factorial is {factorial(num)}')

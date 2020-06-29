# Write a Python function that takes a number as a parameter and check the
# number is prime or not.


def is_prime(num):
    i = 3
    if num % 2 == 0:
        print(f'{num} is not prime')
    elif num == 3:
        print(f'{num} is prime')
    else:
        while (i < num):
            if num % i == 0:
                print(f'{num} is not prime')
                break
            else:
                print(f'{num} is prime')
                break
            i += 2


input_number = int(input("Enter number "))
is_prime(input_number)

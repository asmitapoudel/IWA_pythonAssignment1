# Write a Python program to print the even numbers from a given list.
def print_even(lst):
    return [i for i in lst if i % 2 == 0]


my_list = list(range(1, 20))
print(my_list)
print("Even number list")
print(print_even(my_list))

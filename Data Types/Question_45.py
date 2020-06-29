#  Write a Python program to find the index of an item of a tuple

tup = tuple(range(1, 10))
print(tup)

item = int(input("Enter the number to find index "))
print(f'The index is {tup.index(item)}')

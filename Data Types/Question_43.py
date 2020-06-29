# Write a Python program to remove an item from a tuple.

tup = tuple(range(1, 10))
print(tup)
item = int(input("Enter any item to remove"))
tup = list(tup)
tup.remove(item)
tup = tuple(tup)
print(tup)

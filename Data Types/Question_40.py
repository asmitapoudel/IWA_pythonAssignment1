# Write a Python program to add an item in a tuple

tup = tuple(range(1, 10, 2))
print(tup)
item = int(input("Enter any item to add"))
tup = list(tup)
tup.append(item)
tup = tuple(tup)
print(tup)

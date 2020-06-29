# Write a Python program to sort a list of tuples using Lambda.
lst = [("Mary", 18), ("Carry", 25), ("Harry", 20), ("Darry", 15), ("Larry", 22)]
print(lst)
lst.sort(key=lambda x: x[1])
print("After Sorting")
print(lst)

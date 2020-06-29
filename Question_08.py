# Write a Python function that takes a list and returns a new list with unique elements of the first list.
def create_unique(lst):
    new_lst = list(set(lst))
    return new_lst


list1 = [1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 8, 8]
print(list1)
print("Unique element list")
print(create_unique(list1))

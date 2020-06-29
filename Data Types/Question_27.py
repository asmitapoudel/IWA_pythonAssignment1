# Write a Python program to replace the last element in a list with another list.

list1 = [1, 3, 5, 7, 9, 10]
list2 = [2, 4, 6, 8]
result = list1[:-1] + list2
print(result)
# Write a Python program to insert a given string at the beginning of all items in a list.

number_list = [1, 2, 3, 4]
string1 = 'Emp'

string1 += '{0}'
number_list = [string1.format(i) for i in number_list]
print(number_list)

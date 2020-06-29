# Write a Python script to generate and print a dictionary that contains a
# number (between 1 and n) in the form (x, x*x).

number = int(input("Enter any number "))
dict1 = {}
for i in range(1, number+1):
    dict1.update({i: i*i})
print(dict1)

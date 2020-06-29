#  Write a Python script to print a dictionary where the keys are numbers
# between 1 and 15 (both included) and the values are square of keys

dict1 = {}
for i in range(1, 16):
    dict1.update({i: i*i})
print(dict1)

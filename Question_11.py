# Write a Python program to create a lambda function that adds 15 to a given number passed in
# as an argument, also create a lambda function that multiplies argument x with argument y
# and print the result.

func1 = lambda x: x + 15
func2 = lambda x, y: x * y
print(func1(10))
print(func2(20, 2))

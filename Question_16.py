# Write a Python program to square and cube every number in a given list of integers using Lambda.
num_list = list(range(10))
square = list(map(lambda x: x ** 2, num_list))
cube = list(map(lambda x: x ** 3, num_list))

print(num_list)
print("After Squaring")
print(square)
print("After Cubing")
print(cube)

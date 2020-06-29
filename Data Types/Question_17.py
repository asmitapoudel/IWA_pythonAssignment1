from functools import reduce

input_number = [int(x) for x in input("Enter multiple value: ").split()]
result = reduce(lambda x, y: x * y, input_number)
print(result)

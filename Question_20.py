# Write a Python program to find intersection of two given arrays using Lambda

arr1 = list(range(10))
arr2 = list(range(5, 15))

print(arr1)
print(arr2)

result = list(filter(lambda x: x in arr1, arr2))
print (f'Intersection of array: {result}')

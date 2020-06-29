input_string = list(input("Enter String and index to delete"))
index = int(input())
del input_string[index]
result = "".join(input_string)
print(result)

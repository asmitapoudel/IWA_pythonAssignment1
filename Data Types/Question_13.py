input_string = input("Enter String ").split(',')
input_string = list(set(input_string))
input_string.sort()
print(",".join(input_string))

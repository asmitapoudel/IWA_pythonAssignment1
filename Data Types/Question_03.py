input_string = input("Enter String: ")

first_char = input_string[0]
input_string = input_string.replace(first_char.upper(), '$')
input_string = input_string.replace(first_char.lower(), '$')
input_string = first_char + input_string[1:]

print(input_string)

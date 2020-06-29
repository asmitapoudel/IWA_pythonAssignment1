input_string1 = input("Enter two String: ")
input_string2 = input()

new_string1 = input_string2[:2] + input_string1[2:]
new_string2 = input_string1[:2] + input_string2[2:]

print(f'{new_string1} {new_string2}')

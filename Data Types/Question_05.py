input_string = input("Enter String: ")

if input_string[-3:] == 'ing':
    result = input_string + "ly"
elif len(input_string) >= 3:
    result = input_string + "ing"
else:
    result = input_string

print(result)

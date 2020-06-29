input_string = input("Enter String: ")

if len(input_string) < 2:
    print("Empty String")
else:
    print(input_string[:2] + input_string[-2::])

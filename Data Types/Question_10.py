input_string = input("Enter String:")
result = [input_string[i] for i in range(len(input_string)) if i % 2 == 0]

print("".join(result))

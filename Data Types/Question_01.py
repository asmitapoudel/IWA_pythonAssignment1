input_string = input("Enter String: ").lower()
result_dict = {}
for n in input_string:
    keys = result_dict.keys()
    if n in keys:
        result_dict[n] += 1
    else:
        result_dict[n] = 1

print(result_dict)

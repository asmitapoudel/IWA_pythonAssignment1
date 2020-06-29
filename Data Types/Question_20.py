count = 0
input_string = input("Enter multiple string ").split()
for i in input_string:
    if i[0] == i[-1] and len(i) >=3:
        count += 1
print(count)

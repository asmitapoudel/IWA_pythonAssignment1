# . Write a Python function that accepts a string and calculate the number of
# upper case letters and lower case letters.


def count(str1):
    upper_count = 0
    for i in str1:
        if i.isupper():
            upper_count += 1
    return upper_count


input_string = input("Enter string ")
uc = count(input_string)
print(f'The number of upper case letters = {uc} and lower case = {len(input_string)-uc}')

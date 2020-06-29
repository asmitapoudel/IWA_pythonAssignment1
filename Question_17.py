# Write a Python program to find if a given string starts with a given character using Lambda
check_char = lambda x: True if x.startswith('H') else False
print(check_char('Hello'))

check_char = lambda x: True if x.startswith('K') else False
print(check_char('World'))

#  Write a Python program to check whether a given string is number or not using Lambda.


is_number = lambda x: x.replace('.', '', 1).isdigit()

print(is_number('5847'))
print(is_number('69a36'))

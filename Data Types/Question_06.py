def string_manipulation(str):
    not_index = str.find('not')
    poor_index = str.find('poor')

    if (poor_index > not_index) and (not_index > 0) and (poor_index > 0):
        str = str.replace(str[not_index:(poor_index + 4)], 'poor')
        return str
    else:
        return str


string1 = "The lyrics is not that poor!"
string2 = "The lyrics is poor!"

print(string_manipulation(string1))
print(string_manipulation(string2))


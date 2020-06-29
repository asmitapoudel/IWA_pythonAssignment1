def insert_string_middle(string1, string2):
    return string1[:len(string1)//2] + string2 + string1[len(string1)//2:]


print(insert_string_middle("[[]]", "Python"))
print(insert_string_middle("{{}}", "PHP"))

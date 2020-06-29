def add_tags(tag, string):
    return f'<{tag}>{string}<!{tag}>'


print(add_tags('i', "python"))
print(add_tags('b', "python"))

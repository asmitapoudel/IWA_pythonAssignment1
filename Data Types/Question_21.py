def last(a):
    return a[-1]


number_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
number_list = tuple(number_list)
print(sorted(number_list, key=last))

dict_list1 = [{}, {}, {}]
dict_list2 = [{1,2},{},{}]
print(all(not d for d in dict_list1))
print(all(not d for d in dict_list2))

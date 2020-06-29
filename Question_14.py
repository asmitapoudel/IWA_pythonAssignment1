# Write a Python program to sort a list of dictionaries using Lambda.
lst = [{"name": "Mary", "Age": 18}, {"name": "Cary", "Age": 25}, {"name": "Hary", "Age": 20}, {"name": "Dary", "Age":15}, {"name": "Lary", "Age":22}]
print(lst)
lst.sort(key=lambda x: x["Age"])
print("After Sorting")
print(lst)

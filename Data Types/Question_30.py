#  Write a Python script to check whether a given key already exists in a dictionary
def find_key(dic, key):
    for d in dic:
        if d == key:
            return "Key exist"
        else:
            return "Key Doesnt exist"


dic1 = {"name": "Aqua", "age": 100}

print(find_key(dic1, "name"))
print(find_key(dic1, "address"))

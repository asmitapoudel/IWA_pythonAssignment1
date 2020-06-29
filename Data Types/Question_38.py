#  Write a Python program to remove a key from a dictionary.
dic1 = {"Name": "Aqua", "Age": 100, "Address": "Axel"}
print(dic1)
key = input("Enter key to delete")

if key in dic1:
   del dic1[key]

print(dic1)

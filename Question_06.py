# Write a Python function to check whether a number is in a given range
def check_for_range(num):
    if num in range(7, 50, 3):
        print("Number is in range")
    else:
        print("Number is not in range")


number_list = list(range(7, 50, 3))
print(number_list)
item = int(input("Enter number:"))
check_for_range(item)

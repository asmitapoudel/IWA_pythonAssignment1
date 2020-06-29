number = int(input("Number of Words in list and word"))
word_list = []
word_list_count = []
for _ in range(number):
    word_list.append(input())
    word_list_count.append((len(word_list[_]), word_list[_]))

word_list_count.sort()
print(word_list_count[-1][1])

input_string = input("Enter a sentence")
input_string = input_string.split()
words_count = {}

for word in input_string:
    if word in words_count:
        words_count[word] += 1
    else:
        words_count[word] = 1

print(words_count)

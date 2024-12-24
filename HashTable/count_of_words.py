def count(string_list):
    word_count = {}
    for word in string_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

string_list = input('enter the string: ').split()
print(count(string_list))
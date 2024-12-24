def alphabetCount(string):
    count_map = {}
    for i in string:
        if i in count_map:
            count_map[i] += 1
        elif i.isalpha():
            count_map[i] = 1
    return count_map

string = input('enter the string: ')
print(alphabetCount(string))
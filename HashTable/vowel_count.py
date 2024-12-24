def vowelCount(string):
    vowel = set(['a','e','i','o','u'])
    hash_map = {}
    for i in string:
        if i in hash_map:
            hash_map[i] += 1
        elif i in vowel:
            hash_map[i] = 1
    return hash_map

string = input('enter the string: ')
print(vowelCount(string))
def duplicate(string):
    vow = {'a','e','i','o','u'}
    dic = {}
    for i in string:
        if i in dic:
            dic[i] += 1
        elif i in vow:
            dic[i] = 1
    return dic
    
print(duplicate('aeiouaeiounikhil'))
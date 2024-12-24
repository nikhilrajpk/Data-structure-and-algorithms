def length(data):
    new_dict = {}
    for i in data:
        n = len(i)
        if n in new_dict:
            new_dict[n].append(i)
        else:
            new_dict[n] = [i]
    return new_dict


data = ["cat", "dog", "apple", "bat", "banana"]
print(length(data))
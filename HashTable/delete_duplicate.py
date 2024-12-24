def deleteDuplicate(data):
    val_lst = []
    values_map = {}
    for key,value in data.items():
        if value in values_map:
            values_map[value].append(key)
        else:
            values_map[value] = [key]
    print(values_map)
    for val in values_map.values():
        if len(val) > 1:
            val_lst.append(val)
    print(val_lst)
    
    for i in val_lst:
        for j in i:
            del data[j]
    return data
    


data = {"a": 1, "b": 2, "c": 1}
print(deleteDuplicate(data))
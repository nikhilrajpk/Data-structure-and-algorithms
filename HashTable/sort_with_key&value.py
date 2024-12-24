def key_sort(data):
    lst = [(key,value) for key,value in data.items()]
    lst.sort(key = lambda x:x[0])
    new_data = {key:value for key,value in lst}
    return new_data
def value_sort(data):
    lst = [(key,value) for key,value in data.items()]
    lst.sort(key=lambda x : x[1])
    new_data = {key:value for key,value in lst}
    return new_data
    
data = {"b": 2, "a": 3, "c": 1}
print(key_sort(data))
print(value_sort(data))
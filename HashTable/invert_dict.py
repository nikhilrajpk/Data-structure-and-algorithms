from collections import defaultdict
def invert(data):
    new_data = defaultdict(list)
    for key,val in data.items():
        new_data[val].append(key)
    
    return dict(new_data)

data = {"a": 1, "b": 2, "c": 1}
print(invert(data))
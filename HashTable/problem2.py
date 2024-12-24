# Write a function to merge two dictionaries into one, 
# with the second dictionary's values overwriting any conflicting keys.

def update(data1,data2):
    print(data1)
    print(data2)
    for k,v in data2.items():
        if k in data1:
            data1[k] = v
        else:
            data1[k] = v
    return data1

data1 = {"name": "Alice", "age": 25, "city": "New York"}
data2 = {"name": "Nikhil", "course": 'IT'}
print(update(data1,data2))
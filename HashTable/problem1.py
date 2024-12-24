def add(data,key,value):
    data[key] = value
    return data
def update(data,key,new_value):
    data.update(age=26)
    return data
def remove(data,key):
    del data[key]
    return data
def check(data,key):
    if key in data:
        return True
    else:
        return False

data = {"name": "Alice", "age": 25, "city": "New York"}
print(add(data,'profession','engineer'))
print(update(data,'age',26))
print(remove(data,'city'))
print(check(data,'name'))
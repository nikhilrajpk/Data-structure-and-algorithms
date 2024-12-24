def maxValue(data):
    max_key = ''
    max_value = 0
    for key,value in data.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key
        

data = {"a": 5, "b": 2, "c": 9}
print(maxValue(data))
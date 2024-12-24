# Implement a function to check if two dictionaries are equal
# (i.e., have the same keys and values, regardless of order).

def same(data1,data2):
    for key,val in data1.items():
        if not key in data2:
            return False
        elif key in data2 and val != data2[key]:
            return False
    return True

data1 = {'name':'n','age':1}
data2 = {'name':'n','age':1}
print(same(data1,data2))
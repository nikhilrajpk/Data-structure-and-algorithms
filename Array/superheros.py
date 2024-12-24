def get_length(heros):
    count = 0
    for i in heros:
        count += 1
    return count
def add(heros, new):
    heros.append(new)
    return heros

def insert_after_hulk(heros):
    heros.remove('black panther')
    heros.insert(3,'black panther')
    return heros

def replace_thor_hulk(heros,new):
    heros[1:3] = [new]
    return heros

def sorting(heros):
    heros.sort(key = lambda x : x[-2])
    return heros
    
heros=['spider man','thor','hulk','iron man','captain america']
print('length : ', get_length(heros))
print(add(heros,'black panther'))
print(insert_after_hulk(heros))
print(replace_thor_hulk(heros,'dr strange'))
print(sorting(heros))
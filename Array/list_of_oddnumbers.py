def createList(n):
    odd = [i for i in range(1,n+1,2)]
    return odd

n = int(input('enter the max: '))
print(createList(n))
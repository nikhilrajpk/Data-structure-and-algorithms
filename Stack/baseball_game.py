def calPoints(operations):
    stack = []
    for i in operations:
        if i == '+':
            a = stack[-1]
            b = stack[-2]
            stack.append(a+b)
        elif i == 'D':
            a = stack[-1]
            stack.append(a*2)
        elif i == 'C':
            stack.pop()
        else:
            stack.append(int(i))
    s = sum(stack)
    return s

ops = ["5","2","C","D","+"]
print(calPoints(ops))
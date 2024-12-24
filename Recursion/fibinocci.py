def fib(n):
    a,b,i = 0,1,2
    if n == 1:
        return a
    print(a)
    print(b)
    while i < n:
        a, b = b, a+b 
        print(b)
        i += 1
    return
def fib(n,a,b,i):
    if n == 1:
        return a
    if a == 0 : print(a)
    print(b)
    if i == n:
        return
    return fib(n,b,b+a,i+1)
fib(5, a=0, b=1, i=2)
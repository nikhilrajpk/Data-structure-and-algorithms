def f(n):
    if n <= 1:
        return 
    f(n-1)
    print(n)
    f(n-1)
    
print(f(5))

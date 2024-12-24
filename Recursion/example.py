# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n-1)
    
# print(fact(5))


# def fib(n,a,b,i):
#     if n == 1:
#         print(a)
#         return
#     if a == 0:
#         print(a)
#     print(b)
#     if i == n:
#         return
#     return fib(n,b,a+b,i+1)
    
# fib(5,a=0,b=1,i=2)


def sumdigit(num,total):
    if num == 0:
        return total
    total += num%10
    return sumdigit(num//10,total)
    
print(sumdigit(123,total = 0))
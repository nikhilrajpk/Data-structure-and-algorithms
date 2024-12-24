def fact_recursion(n):
    if n <= 1:
        return 1
    return n * fact_recursion(n-1)

print(fact_recursion(3))
""" fact_recursion.
Time complexity : O(n) because of the recursion happens n times.
Space complexity : O(n) because of the call stack frame used in recursion.
"""
def fact_iter(n):
    s = 1
    for i in range(1,n+1):
        s *= i
    return s

print(fact_iter(3))
""" fact_recursion.
Time complexity : O(n) because of the for loop.
Space complexity : O(1) no additional memory used rather than storing the factorial in s.
"""
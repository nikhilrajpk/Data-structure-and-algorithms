def sum_of_digits(num):
    s = 0
    while num > 0:
        s += num%10
        num = num//10
    return s

"""_summary_
Time Complexity: 𝑂(𝑑), where 𝑑 is the number of digits in num.Each recursive call processes one digit of num.
Space Complexity: 𝑂(𝑑), due to the recursion stack. For each recursive call, a new stack frame is created.
"""

def sum_of_digits(num,n):
    if num == 0:
        return n
    n += num % 10
    return sum_of_digits((num//10),n)

print(sum_of_digits(123,n=0))
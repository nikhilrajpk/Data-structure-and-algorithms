from collections import deque
def reverse(string):
    stack = deque()
    for i in string:
        stack.append(i)
    while stack:
        print(stack.pop(),end='')
        # yield stack.pop()
string = 'we will conquere covi-19'
rev = reverse(string)
# for char in rev:
#     print(char,end='')